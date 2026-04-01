# Urban Transit Delay Analysis

## Milestone 5.5 — Installing Python and Anaconda

### Overview

This milestone marks the first technical step of the Urban Transit Delay Analysis project. Before any data can be loaded, cleaned, or analyzed, a stable and reproducible development environment must be in place. This section documents the complete setup process — from downloading Anaconda to verifying that all core data science libraries are installed and accessible inside a dedicated project environment.

The goal of this setup is to ensure that every subsequent milestone — including data loading, exploratory analysis, visualization, and modeling — runs without environment-related errors or version conflicts.

---

### System Information

| Property | Details |
|---|---|
| Operating System | Windows 11 |
| Python Version | 3.11.15 |
| Anaconda Version | Anaconda3 2025.12-2 |
| Conda Version | 25.11.1 |
| Environment Name | transit-analysis |
| Environment Location | D:\CHOTU C\envs\transit-analysis |

---

### Steps Followed

**Step 1 — Downloaded Anaconda**

Visited the official Anaconda website at `https://www.anaconda.com/download` and downloaded the Windows 64-bit installer (`Anaconda3-2025.12-2-Windows-x86_64.exe`). The file was approximately 800 MB and was downloaded over a stable WiFi connection.

**Step 2 — Installed Anaconda**

Ran the installer with the following choices:
- Installation type: Just Me
- Installation path: default system path
- Advanced options: left "Add Anaconda to PATH" unchecked (as recommended)
- Kept "Register Anaconda3 as default Python 3.13" checked so tools like VS Code can detect Python automatically

Installation completed successfully with no errors.

**Step 3 — Verified base installation**

Opened Anaconda Prompt from the Windows Start Menu and ran the following commands to confirm the base installation was working:
```bash

--theirs picked the wrong README — it took the empty main one instead of your detailed one. Let's restore your full README right now:

Step 1 — Open README.md and paste your full content back
Open the file in VS Code or Notepad:
code README.md
or
notepad README.md
Delete everything in it and paste this complete README back:

markdown# Urban Transit Delay Analysis

## Milestone 5.5 — Installing Python and Anaconda

### Overview

This milestone marks the first technical step of the Urban Transit Delay Analysis project. Before any data can be loaded, cleaned, or analyzed, a stable and reproducible development environment must be in place. This section documents the complete setup process — from downloading Anaconda to verifying that all core data science libraries are installed and accessible inside a dedicated project environment.

The goal of this setup is to ensure that every subsequent milestone — including data loading, exploratory analysis, visualization, and modeling — runs without environment-related errors or version conflicts.

---

### System Information

| Property | Details |
|---|---|
| Operating System | Windows 11 |
| Python Version | 3.11.15 |
| Anaconda Version | Anaconda3 2025.12-2 |
| Conda Version | 25.11.1 |
| Environment Name | transit-analysis |
| Environment Location | D:\CHOTU C\envs\transit-analysis |

---

### Steps Followed

**Step 1 — Downloaded Anaconda**

Visited the official Anaconda website at `https://www.anaconda.com/download` and downloaded the Windows 64-bit installer (`Anaconda3-2025.12-2-Windows-x86_64.exe`). The file was approximately 800 MB and was downloaded over a stable WiFi connection.

**Step 2 — Installed Anaconda**

Ran the installer with the following choices:
- Installation type: Just Me
- Installation path: default system path
- Advanced options: left "Add Anaconda to PATH" unchecked (as recommended)
- Kept "Register Anaconda3 as default Python 3.13" checked so tools like VS Code can detect Python automatically

Installation completed successfully with no errors.

**Step 3 — Verified base installation**

Opened Anaconda Prompt from the Windows Start Menu and ran the following commands to confirm the base installation was working:
```bash
python --version
# Output: Python 3.13.9

conda --version
# Output: conda 25.11.1

conda list
# Output: full list of 300+ packages including pandas, numpy, matplotlib, jupyter
```

**Step 4 — Created a dedicated project environment**

To keep this project isolated from the base environment and avoid package conflicts, a separate Conda environment was created specifically for the transit delay analysis work:
```bash
conda create --name transit-analysis python=3.11
```

This created a clean environment with Python 3.11.15 located at `D:\CHOTU C\envs\transit-analysis`.

**Step 5 — Activated the environment and installed libraries**
```bash
conda activate transit-analysis

conda install pandas numpy matplotlib jupyter -y
```

After activation, the terminal prompt changed from `(base)` to `(transit-analysis)`, confirming the environment switch was successful. All four core libraries were downloaded and installed successfully inside this environment.

**Step 6 — Final verification inside transit-analysis**
```bash
conda list | findstr "pandas numpy matplotlib jupyter"
```

Output confirmed:
- `pandas 3.0.1`
- `numpy 2.4.3`
- `matplotlib 3.10.8`
- `jupyter 1.1.1`
- `jupyterlab 4.5.3`

---

### Why a Separate Environment?

A dedicated `transit-analysis` environment ensures that package versions used in this project do not interfere with other Python projects on the same machine. It also makes the project reproducible — anyone cloning this repository can recreate the exact same environment using the `environment.yml` file that will be added in a later milestone.

---

### Environment Status

| Library | Version | Purpose |
|---|---|---|
| pandas | 3.0.1 | Transit data loading and cleaning |
| numpy | 2.4.3 | Numerical operations on delay data |
| matplotlib | 3.10.8 | Visualizing delay patterns and trends |
| jupyter | 1.1.1 | Interactive analysis notebooks |
| jupyterlab | 4.5.3 | Enhanced notebook interface |

---

### Next Step

With the environment fully configured, the next milestone (5.6) will verify Jupyter launch, confirm notebook execution, and begin building the project folder structure for the transit delay analysis pipeline.
```

---

### Step 2 — Save the file then run these commands
```
git add README.md
```
```
git commit -m "fix: restore complete milestone 5.5 README documentation"
```
```
git push origin assignment-5.5