#!/usr/bin/env python3
"""
Compare FreeSurfer 8 global measures vs sum of 68 DK ROIs (cortical volume only).

- Global: CortexVol from stats/aseg.stats (total cortical gray matter).
- Sum of DK: sum of GrayVol from stats/lh.aparc.stats + stats/rh.aparc.stats (68 regions).

Usage:
  python compare_global_vs_sum_DK.py <subject_dir>
  python compare_global_vs_sum_DK.py /path/to/subject

Subject dir must contain: stats/aseg.stats, stats/lh.aparc.stats, stats/rh.aparc.stats
"""

import re
import sys
from pathlib import Path
from typing import Optional


def read_aseg_cortex_vol(stats_path: Path) -> Optional[float]:
    """Parse aseg.stats for CortexVol (total cortical gray matter), mm^3."""
    text = stats_path.read_text()
    # # Measure Cortex, CortexVol, Total cortical gray matter volume, 396517.747122, mm^3
    m = re.search(r"# Measure Cortex, CortexVol, [^,]+, ([0-9.]+), mm\^3", text)
    return float(m.group(1)) if m else None


def read_aparc_sum_vol(stats_path: Path) -> float:
    """Sum GrayVol from aparc.stats table (34 regions per hemisphere)."""
    lines = stats_path.read_text().splitlines()
    total = 0.0
    for line in lines:
        if line.startswith("#"):
            continue
        parts = line.split()
        # ColHeaders: StructName NumVert SurfArea GrayVol ThickAvg ...
        if len(parts) >= 4:
            try:
                total += float(parts[3])  # GrayVol
            except ValueError:
                continue
    return total


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    subject_dir = Path(sys.argv[1]).resolve()
    stats_dir = subject_dir / "stats"
    aseg = stats_dir / "aseg.stats"
    lh_aparc = stats_dir / "lh.aparc.stats"
    rh_aparc = stats_dir / "rh.aparc.stats"
    for f in (aseg, lh_aparc, rh_aparc):
        if not f.exists():
            print(f"Missing: {f}")
            sys.exit(2)

    cortex_vol_global = read_aseg_cortex_vol(aseg)
    lh_sum = read_aparc_sum_vol(lh_aparc)
    rh_sum = read_aparc_sum_vol(rh_aparc)
    sum_dk = lh_sum + rh_sum

    print(f"Subject: {subject_dir.name}")
    print(f"  Global (aseg.stats)  CortexVol : {cortex_vol_global:,.2f} mm³")
    print(f"  Sum of 68 DK (aparc) GrayVol   : {sum_dk:,.2f} mm³  (lh: {lh_sum:,.2f} + rh: {rh_sum:,.2f})")
    if cortex_vol_global is not None and cortex_vol_global > 0:
        diff = sum_dk - cortex_vol_global
        pct = 100.0 * diff / cortex_vol_global
        print(f"  Difference (sum_DK - global): {diff:+,.2f} mm³  ({pct:+.4f}%)")
        print(f"  Ratio (sum_DK / global)    : {sum_dk / cortex_vol_global:.6f}")


if __name__ == "__main__":
    main()
