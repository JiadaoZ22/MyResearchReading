#!/usr/bin/env python3
"""
Comprehensive script to extract brain ROI relative volume data from PDF files and generate JSON
This script manually extracts data based on the observed patterns in the PDF files
"""

import PyPDF2
import json
import re
import os
import math
from datetime import datetime
from typing import Dict, Any, List, Tuple

class BrainROIDataExtractor:
    def __init__(self):
        self.rois = [
            "Hippocampus", "ntorhinal Cortex", "Temporal Lobes", "Parietal Lobes",
            "Amygdala", "Basal Forebrain", "Accumbens", "Ventral DC", "Lateral Ventricle"
        ]
        self.races = ["White", "Black", "Eastern Asian", "Hispanic/Latinx"]
        self.sexes = ["Male", "Female"]
        self.age_ranges = ["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89"]
        
    def extract_source_from_filename(self, filename: str) -> str:
        """Extract source name from PDF filename"""
        name = filename.replace("BrainROIsRelVol_", "").replace(".pdf", "")
        return name
    
    def parse_volume_range(self, volume_str: str) -> Tuple[float, float]:
        """Parse volume range string like '0.60–0.72%' or '7.8–9.0%'"""
        try:
            # Remove percentage sign and split by dash
            clean_str = volume_str.replace('%', '').strip()
            
            # Handle different dash types (–, -, etc.)
            if '–' in clean_str:
                parts = clean_str.split('–')
            elif '-' in clean_str:
                parts = clean_str.split('-')
            else:
                return float('nan'), float('nan')
            
            if len(parts) != 2:
                return float('nan'), float('nan')
                
            min_val = float(parts[0].strip())
            max_val = float(parts[1].strip())
            
            return min_val, max_val
            
        except (ValueError, IndexError):
            return float('nan'), float('nan')
    
    def extract_data_from_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """Extract ROI data from a single PDF file"""
        source = self.extract_source_from_filename(os.path.basename(pdf_path))
        print(f"Processing {source}...")
        
        data = {}
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                full_text = ""
                
                # Extract all text from all pages
                for page in pdf_reader.pages:
                    full_text += page.extract_text() + "\n"
                
                # Process each ROI
                for roi in self.rois:
                    roi_data = self.extract_roi_data(full_text, roi, source)
                    if roi_data:
                        data[roi] = roi_data
                        total_entries = sum(len(race_data) for race_data in roi_data.values())
                        print(f"  Found data for {roi}: {total_entries} entries")
                        
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            
        return data
    
    def extract_roi_data(self, text: str, roi: str, source: str) -> Dict[str, Any]:
        """Extract data for a specific ROI from text using manual pattern matching"""
        roi_data = {}
        
        # Split text into lines
        lines = text.split('\n')
        
        # Look for ROI sections and extract data
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines
            if not line:
                i += 1
                continue
            
            # Look for race/sex/age patterns
            # Pattern: "White Male10-" or "White Male 10-19" or "White Male10-19"
            race_sex_age_patterns = [
                r'(White|Black|Eastern Asian|Hispanic/Latinx)\s+(Male|Female)(\d+)-(\d+)',
                r'(White|Black|Eastern Asian|Hispanic/Latinx)\s+(Male|Female)\s+(\d+)-(\d+)',
                r'(White|Black|Eastern Asian|Hispanic/Latinx)\s+(Male|Female)(\d+)-',
            ]
            
            race_match = None
            for pattern in race_sex_age_patterns:
                race_match = re.search(pattern, line)
                if race_match:
                    break
            
            if race_match:
                race = race_match.group(1)
                sex = race_match.group(2)
                
                # Handle age extraction
                if len(race_match.groups()) >= 4:
                    age_start = race_match.group(3)
                    age_end = race_match.group(4)
                    age = f"{age_start}-{age_end}"
                else:
                    # Age might be split across lines
                    age_start = race_match.group(3)
                    # Look for age end in current or next line
                    age_end = None
                    for j in range(i, min(i + 2, len(lines))):
                        age_end_match = re.search(r'(\d+)', lines[j])
                        if age_end_match:
                            age_end = age_end_match.group(1)
                            break
                    
                    if age_end:
                        age = f"{age_start}-{age_end}"
                    else:
                        age = f"{age_start}-{int(age_start)+9}"  # Default 10-year range
                
                # Look for ROI name and volume in current or next lines
                volume_found = False
                for j in range(i, min(i + 3, len(lines))):
                    check_line = lines[j].strip()
                    
                    # Look for ROI name and volume pattern
                    if roi.lower() in check_line.lower():
                        # Extract volume range
                        volume_patterns = [
                            r'([0-9.–]+%)',
                            r'([0-9]+\.[0-9]+)–([0-9]+\.[0-9]+)%',
                            r'([0-9]+\.[0-9]+)-([0-9]+\.[0-9]+)%'
                        ]
                        
                        for vol_pattern in volume_patterns:
                            vol_match = re.search(vol_pattern, check_line)
                            if vol_match:
                                if len(vol_match.groups()) == 2:
                                    volume_range = f"{vol_match.group(1)}–{vol_match.group(2)}%"
                                else:
                                    volume_range = vol_match.group(1)
                                
                                # Parse volume range
                                min_vol, max_vol = self.parse_volume_range(volume_range)
                                
                                # Store data
                                self.store_data(roi_data, race, sex, age, min_vol, max_vol, source)
                                volume_found = True
                                break
                        
                        if volume_found:
                            break
                
                if volume_found:
                    i += 1  # Move to next line
                    continue
            
            i += 1
        
        return roi_data
    
    def store_data(self, roi_data: Dict[str, Any], race: str, sex: str, age: str, min_vol: float, max_vol: float, source: str):
        """Store extracted data in the nested structure"""
        # Initialize nested structure
        if race not in roi_data:
            roi_data[race] = {}
        if sex not in roi_data[race]:
            roi_data[race][sex] = {}
        if age not in roi_data[race][sex]:
            roi_data[race][sex][age] = {}
        
        # Store data
        roi_data[race][sex][age][source] = {
            "RelVol_min": min_vol,
            "RelVol_max": max_vol
        }
    
    def process_all_pdfs(self, directory: str) -> Dict[str, Any]:
        """Process all PDF files in the directory"""
        pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
        
        if not pdf_files:
            print("No PDF files found in directory")
            return {}
            
        print(f"Found {len(pdf_files)} PDF files: {pdf_files}")
        
        # Initialize the main data structure
        main_data = {
            "MetaData": {
                "Description": "Brain ROI relative volume data for normal population extracted from AI model outputs",
                "Time": datetime.now().isoformat(),
                "Sources": [],
                "ROIs": self.rois,
                "Races": self.races,
                "Sexes": self.sexes,
                "AgeRanges": self.age_ranges
            },
            "NormalPopulation": {}
        }
        
        # Process each PDF
        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory, pdf_file)
            source = self.extract_source_from_filename(pdf_file)
            main_data["MetaData"]["Sources"].append(source)
            
            pdf_data = self.extract_data_from_pdf(pdf_path)
            
            # Merge data into main structure
            for roi, roi_data in pdf_data.items():
                if roi not in main_data["NormalPopulation"]:
                    main_data["NormalPopulation"][roi] = {}
                
                for race, race_data in roi_data.items():
                    if race not in main_data["NormalPopulation"][roi]:
                        main_data["NormalPopulation"][roi][race] = {}
                    
                    for sex, sex_data in race_data.items():
                        if sex not in main_data["NormalPopulation"][roi][race]:
                            main_data["NormalPopulation"][roi][race][sex] = {}
                        
                        for age, age_data in sex_data.items():
                            if age not in main_data["NormalPopulation"][roi][race][sex]:
                                main_data["NormalPopulation"][roi][race][sex][age] = {}
                            
                            # Merge source data
                            main_data["NormalPopulation"][roi][race][sex][age].update(age_data)
        
        return main_data
    
    def fill_missing_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Fill missing combinations with NaN values"""
        sources = data["MetaData"]["Sources"]
        
        for roi in self.rois:
            if roi not in data["NormalPopulation"]:
                data["NormalPopulation"][roi] = {}
                
            for race in self.races:
                if race not in data["NormalPopulation"][roi]:
                    data["NormalPopulation"][roi][race] = {}
                    
                for sex in self.sexes:
                    if sex not in data["NormalPopulation"][roi][race]:
                        data["NormalPopulation"][roi][race][sex] = {}
                        
                    for age in self.age_ranges:
                        if age not in data["NormalPopulation"][roi][race][sex]:
                            data["NormalPopulation"][roi][race][sex][age] = {}
                            
                        # Fill missing sources with NaN
                        for source in sources:
                            if source not in data["NormalPopulation"][roi][race][sex][age]:
                                data["NormalPopulation"][roi][race][sex][age][source] = {
                                    "RelVol_min": float('nan'),
                                    "RelVol_max": float('nan')
                                }
        
        return data

def main():
    """Main function to run the extraction"""
    extractor = BrainROIDataExtractor()
    
    # Get current directory
    current_dir = os.getcwd()
    print(f"Processing PDFs in: {current_dir}")
    
    # Extract data from all PDFs
    data = extractor.process_all_pdfs(current_dir)
    
    if not data:
        print("No data extracted. Exiting.")
        return
    
    # Fill missing data with NaN
    data = extractor.fill_missing_data(data)
    
    # Save to JSON file
    output_file = "BrainROIs_RelativeVolume_NormalPopulation_Comprehensive.json"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\nData successfully extracted and saved to: {output_file}")
        print(f"Total ROIs processed: {len(data['NormalPopulation'])}")
        print(f"Sources: {', '.join(data['MetaData']['Sources'])}")
        
        # Count actual data entries
        total_entries = 0
        non_nan_entries = 0
        for roi in data['NormalPopulation']:
            for race in data['NormalPopulation'][roi]:
                for sex in data['NormalPopulation'][roi][race]:
                    for age in data['NormalPopulation'][roi][race][sex]:
                        for source in data['NormalPopulation'][roi][race][sex][age]:
                            total_entries += 1
                            entry = data['NormalPopulation'][roi][race][sex][age][source]
                            if not (str(entry['RelVol_min']) == 'nan' and str(entry['RelVol_max']) == 'nan'):
                                non_nan_entries += 1
        
        print(f"Total entries: {total_entries}")
        print(f"Non-NaN entries: {non_nan_entries}")
        
        # Show sample data
        print("\nSample data:")
        sample_roi = "Hippocampus"
        sample_race = "White"
        sample_sex = "Male"
        sample_age = "10-19"
        sample_source = "Sonnet4"
        
        try:
            sample_data = data['NormalPopulation'][sample_roi][sample_race][sample_sex][sample_age][sample_source]
            print(f"{sample_roi}, {sample_race}, {sample_sex}, {sample_age}, {sample_source}:")
            print(f"  Min: {sample_data['RelVol_min']}, Max: {sample_data['RelVol_max']}")
        except KeyError:
            print("Sample data not found")
        
    except Exception as e:
        print(f"Error saving JSON file: {e}")

if __name__ == "__main__":
    main()
