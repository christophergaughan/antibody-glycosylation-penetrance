# antibody-glycosylation-penetrance

**Empirically-validated glycosylation penetrance tables for antibody variable domains, with independent refutation of the Melo-Braga H/Q blocker rule.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Key Findings

Analysis of 19,265 PDB structures containing 2,203 variable domain sequons reveals:

| Finding | Melo-Braga (2024) | This Study | Implication |
|---------|-------------------|------------|-------------|
| **Q is blocker** | 0/11 (0%) | 2/79 (2.5%) | ❌ **Refuted** — Q reduces but does not block |
| **H is blocker** | 0/6 (0%) | 0/81 (0%) | ✅ Confirmed |
| **VH = VL risk** | Not tested | VL 60% higher (p=0.012) | Chain-specific scanning required |
| **S = T risk** | Not tested | T 4.4× higher than S | Third position matters |

**Both Q glycosylation events occur in our independent (decontaminated) dataset** — this is not an artifact of re-analyzing Melo-Braga's data.

---

## Why This Matters

ML tools like RFdiffusion generate antibody sequences without considering post-translational modifications. Van de Bovenkamp et al. (2016) showed that 15-25% of circulating IgG carries Fab glycosylation, acquired through somatic hypermutation. When ML tools recapitulate these sequons without the evolutionary selection context, the resulting antibodies may have:

- Heterogeneous glycoform populations
- Altered binding kinetics
- Reduced stability
- Immunogenicity risk
- Manufacturing variability

This dataset provides the empirical penetrance values needed to triage ML-designed sequences for glycosylation liability.

---

## Quick Start

```python
import pandas as pd

# Load penetrance lookup tables
x_residue = pd.read_csv('data/scanner_x_residue_lookup.csv', index_col=0)
region = pd.read_csv('data/scanner_region_lookup.csv', index_col=0)
chain_x = pd.read_csv('data/scanner_chain_x_lookup.csv', index_col=[0,1])

# Check risk for a sequon with X=Q in VL
risk = chain_x.loc[('VL', 'Q'), 'penetrance']  # Returns 0.043 (4.3%)
```

---

## Risk Hierarchy

```
BLOCKED (<1%):     H, P
LOW (1-3%):        K, W, N, G, Y, V, Q(VH)
MODERATE (3-10%):  Q(VL), A, F, S, M, C, T, L
HIGH (10-20%):     D, R, I
EXTREME (>20%):    I in FR1 (40%), position 20 (37%)
```

**Regional risk:** FR1 > FR4 > FR3 >> CDR1 > CDR3 > CDR2 ≈ FR2

**Chain effect:** VL baseline 7.2% vs VH baseline 4.5%

**Third position:** N-X-T (10.2%) >> N-X-S (2.3%)

---

## Repository Contents

```
antibody-glycosylation-penetrance/
├── README.md
├── LICENSE
├── paper/
│   └── intro_methods.md          # Manuscript Introduction & Methods
├── data/
│   ├── PDB_validation_FINAL_dataset.parquet    # Complete sequon dataset
│   ├── scanner_x_residue_lookup.csv            # X-residue penetrance
│   ├── scanner_region_lookup.csv               # Regional penetrance
│   ├── scanner_chain_x_lookup.csv              # Chain × X-residue
│   ├── scanner_position_lookup.csv             # IMGT position-specific
│   └── scanner_third_pos_lookup.csv            # S vs T effect
├── notebooks/
│   └── ALL_Data_penetrance.ipynb               # Full analysis (Colab)
└── figures/
    ├── x_residue_penetrance.png                # Fig 1: X-residue risk
    ├── vh_vl_analysis.png                      # Fig 2: Chain effects
    ├── penetrance_by_region.png                # Fig 3: Regional risk
    └── melo_braga_vs_validation.png            # Fig 4: Dataset comparison
```

---

## Figures to Include

Upload these PNGs from your notebook output (filenames will have date suffix):

| Figure | Notebook Output | Shows |
|--------|-----------------|-------|
| **Fig 1** | `x_residue_penetrance_YYYYMMDD.png` | X-residue risk ranking with H/Q highlighted |
| **Fig 2** | `vh_vs_vl_analysis_YYYYMMDD.png` | Chain-specific penetrance comparison |
| **Fig 3** | `penetrance_by_region_sensitivity_YYYYMMDD.png` | Regional risk with bias correction |
| **Fig 4** | `melo_braga_vs_validation_YYYYMMDD.png` | Side-by-side dataset comparison |

---

## Dataset Details

### Ascertainment Bias

| Dataset | Bias Direction | Penetrance | Interpretation |
|---------|----------------|------------|----------------|
| Melo-Braga | Enriched (sought glyco) | 35.1% | Upper bound |
| This study | Depleted (crystallographers avoid glyco) | 5.1% | Lower bound |
| True population | — | ~10-20% | Estimated |

### Decontaminated Validation

To ensure independence from Melo-Braga's dataset:
- Excluded all 6,709 PDB IDs from their Supplementary Table 1A
- Remaining: 322 PDBs, 903 sequons, 33 glycosylated (3.7%)
- **Critical:** Both Q glycosylation events (2/53 = 3.8%) are in this independent set

---

## Methods Summary

1. **PDB Query:** All human antibody structures (X-ray/cryo-EM, ≤3.5 Å resolution)
2. **Sequon Detection:** N-X-S/T where X ≠ P
3. **Glycosylation Detection:** Carbohydrate residues within 2.0 Å of Asn Nδ
4. **Numbering:** IMGT via ANARCII 2.0.3
5. **Statistics:** Fisher's exact test, Wilson CIs, Bayesian logistic regression (PyMC)

See `paper/intro_methods.md` for full methodology.

---

## Citation

If you use this dataset or findings, please cite:

```bibtex
@misc{antibody_glyco_penetrance_2025,
  author = {[Your Name]},
  title = {Independent Validation of N-linked Glycosylation Penetrance in Antibody Variable Domains},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/[username]/antibody-glycosylation-penetrance}
}
```

### Related Work

- Melo-Braga MN et al. (2024) "N-glycosylation in the variable domain of antibodies" — the dataset we validate and extend
- van de Bovenkamp FS et al. (2016) "The emerging importance of IgG Fab glycosylation in immunity" — biological context for SHM-introduced glycosylation

---

## License

MIT License — use freely with attribution.

---

## Contact

Questions or collaboration inquiries: [your email or LinkedIn]
