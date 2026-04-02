## Milestone 5.7 — Launching Jupyter Notebook and Understanding the Home Interface

### Launch Details

| Property | Details |
|---|---|
| Environment used | transit-analysis |
| Python version | 3.11.15 |
| Jupyter Notebook version | 7.5.3 |
| Launch command | `jupyter notebook` |
| Launch directory | project root folder |
| Localhost URL | http://localhost:8888 |

### Interface Sections Identified
- File browser area — lists all files and folders in the project root
- Navigation breadcrumb — shows current directory path
- New button — creates notebooks, folders, and text files
- File type icons — distinguishes folders, notebooks (.ipynb), and scripts

### Folder Navigation
Created a notebooks/ folder from within the Jupyter interface. Practiced navigating into and out of the folder using breadcrumbs. Confirmed that the working directory always reflects the folder from which Jupyter was launched.

### Notebook Created
Created `notebooks/jupyter_interface_exploration.ipynb` with:
- A markdown cell documenting the project context
- A code cell confirming environment and kernel details
- Kernel verified as Python 3 (ipykernel) from transit-analysis environment

### Troubleshooting Notes
- If Jupyter does not launch: verify transit-analysis environment is active using `conda activate transit-analysis`
- If kernel shows as disconnected: click Kernel menu → Restart Kernel
- If browser does not open: manually paste the localhost URL from the terminal into Chrome

### Status: Jupyter workspace confirmed and navigated successfully