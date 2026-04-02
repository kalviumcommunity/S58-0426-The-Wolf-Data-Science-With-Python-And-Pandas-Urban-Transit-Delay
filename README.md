## Milestone 5.6 — Verifying Python, Conda, and Jupyter

### Verification Summary

| Check | Command | Result |
|---|---|---|
| Python version | `python --version` | Python 3.11.15 |
| Conda version | `conda --version` | conda 25.11.1 |
| Active environment | `conda env list` | transit-analysis * |
| Key packages | `conda list` | pandas, numpy, matplotlib, jupyter confirmed |
| Jupyter launch | `jupyter lab` | Opened at localhost:8888 |
| Notebook execution | Shift+Enter on cells | All cells ran without errors |

### Python REPL Verification
Launched Python shell and ran print statement, arithmetic, and sys.version — all returned correct outputs confirming Python 3.11.15 is stable.

### Jupyter Verification
Launched JupyterLab from inside transit-analysis environment. Created notebook `environment_verification.ipynb` and ran 3 cells confirming pandas, numpy, matplotlib imports work correctly and a transit delay bar chart renders without errors.

### Status: Environment Verified and Sprint-Ready