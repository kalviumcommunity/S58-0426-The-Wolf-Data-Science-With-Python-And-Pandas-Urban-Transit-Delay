# missing_values_transit.py
# Milestone 5.33 - Detecting Missing Values
#                  in DataFrames
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate detection, counting, and
#          inspection of missing values using
#          transit domain data

import pandas as pd
import numpy as np
import os

print("=" * 57)
print("  MILESTONE 5.33 - DETECTING MISSING VALUES")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Create dataset WITH missing values
# Real transit datasets always have gaps
# We intentionally introduce missing values to
# demonstrate detection techniques
# ─────────────────────────────────────────────────────

print("\n--- SETUP: Creating Transit Dataset ---")
print("(with realistic missing values)\n")

# Build dataset with intentional missing values
# NaN = Not a Number — Pandas standard for missing
data = {
    "trip_id": [
        "T001","T002","T003","T004","T005",
        "T006","T007","T008","T009","T010",
        "T011","T012","T013","T014","T015",
        "T016","T017","T018","T019","T020",
        "T021","T022","T023","T024","T025"
    ],
    "route_id": [
        "Route_42", "Route_7",  None,       # T003 missing
        "Route_23", "Route_42", "Route_7",
        None,        "Route_23", "Route_42", # T007 missing
        "Route_7",  "Route_15", "Route_23",
        "Route_42", None,        "Route_15", # T014 missing
        "Route_23", "Route_42", "Route_7",
        "Route_15", "Route_23", "Route_42",
        "Route_7",  None,        "Route_15", # T023 missing
        "Route_23"
    ],
    "day_of_week": [
        "Monday","Monday","Tuesday","Tuesday",
        "Wednesday","Wednesday","Thursday","Thursday",
        "Friday","Friday","Monday","Tuesday",
        "Wednesday","Thursday","Friday","Monday",
        "Tuesday","Wednesday","Thursday","Friday",
        "Monday","Tuesday","Wednesday","Thursday",
        "Friday"
    ],
    "hour_of_day": [
        8, 9, 7, 8, 17, 18, 8, 7,
        9, 17, 8, 18, 7, 9, 8, 17,
        None, 8, 7, 9,              # T017 missing
        8, 17, 18, None, 7          # T024 missing
    ],
    "delay_minutes": [
        14,  31,  5,   0,   22,
        34,  3,   2,   18,  18,
        None, 1,  21,  34,  None,   # T011, T015 missing
        3,   37,  2,   4,   14,
        17,  None, 8,  22,  11      # T022 missing
    ],
    "status": [
        "Minor Delay",  "Severe Delay", "On Time",
        "On Time",      "Major Delay",  "Severe Delay",
        "On Time",      "On Time",      "Major Delay",
        "Major Delay",  None,           "On Time",  # T011
        "Major Delay",  "Severe Delay", None,       # T015
        "On Time",      "Severe Delay", "On Time",
        "On Time",      "Minor Delay",  "Minor Delay",
        None,           "Minor Delay",  "Major Delay", # T022
        "Minor Delay"
    ],
    "passenger_count": [
        42,  None, 38,  55,  61,         # T002 missing
        None, 29,  44,  None, 57,        # T006,T009 missing
        33,  48,  None, 62,  41,         # T013 missing
        None, 39,  52,  47,  None,       # T016,T020 missing
        44,  58,  None, 37,  None        # T023,T025 missing
    ]
}

df = pd.DataFrame(data)

print(f"Dataset created      : {len(df)} rows, "
      f"{len(df.columns)} columns")
print(f"Columns              : "
      f"{list(df.columns)}")
print()
print("Missing values were intentionally added to")
print("simulate a realistic raw transit dataset.")

# ─────────────────────────────────────────────────────
# SECTION 1 - UNDERSTANDING MISSING VALUES
# NaN = Not a Number (float type)
# None = Python's null object
# Pandas treats both as missing
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Understanding Missing Values ---")
print()

print("How missing values appear in Pandas:")
print()

# Show first few rows — NaN visible
print("df.head(8) — NaN visible in the table:")
print(df.head(8).to_string())

print()
print("Missing value representations in Pandas:")
print(f"  np.nan  : {np.nan} — float type, "
      f"used for numeric columns")
print(f"  None    : {None}  — Python null, "
      f"used for object columns")
print(f"  Both treated as missing by pd.isnull()")

# Demonstrate both are detected
print()
test_series = pd.Series([1, None, np.nan, 4, None])
print(f"Test series : {list(test_series)}")
print(f"isnull()    : {list(test_series.isnull())}")
print("Both None and NaN detected as missing → True")

# ─────────────────────────────────────────────────────
# SECTION 2 - DETECTING MISSING VALUES
# isnull() returns boolean DataFrame
# True  = value is missing
# False = value is present
# notnull() is the inverse
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Detecting Missing Values ---")
print()

# isnull() on full DataFrame — boolean mask
print("2a. df.isnull() — boolean mask "
      "(first 8 rows):")
print(df.isnull().head(8).to_string())

print()
print("  True  = missing value at that position")
print("  False = value is present")

# isnull() on single column
print("\n2b. df['delay_minutes'].isnull() "
      "— single column:")
delay_null = df['delay_minutes'].isnull()
print(f"  {list(delay_null)}")
print(f"  Missing positions: "
      f"{list(delay_null[delay_null].index)}")

# notnull() — inverse
print("\n2c. df['delay_minutes'].notnull() "
      "— inverse check:")
delay_not_null = df['delay_minutes'].notnull()
print(f"  Present positions: "
      f"{list(delay_not_null[delay_not_null].index)}")

# ─────────────────────────────────────────────────────
# SECTION 3 - COUNTING MISSING VALUES
# sum() on boolean Series counts True values
# (True = 1, False = 0)
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Counting Missing Values ---")
print()

# Count per column
missing_per_col = df.isnull().sum()
print("3a. df.isnull().sum() — missing per column:")
print()
print(f"  {'Column':<20} {'Missing':>8} "
      f"{'Out of':>8} {'Percent':>9}")
print("  " + "-" * 48)

for col in df.columns:
    missing = df[col].isnull().sum()
    total   = len(df)
    pct     = (missing / total) * 100
    bar     = "█" * missing + "░" * (total - missing)
    print(f"  {col:<20} {missing:>8} "
          f"{total:>8} {pct:>8.1f}%")

# Total missing across entire DataFrame
total_missing = df.isnull().sum().sum()
total_cells   = df.shape[0] * df.shape[1]
overall_pct   = (total_missing / total_cells) * 100

print()
print(f"3b. Total missing values:")
print(f"  Missing cells  : {total_missing}")
print(f"  Total cells    : {total_cells}")
print(f"  Missing rate   : {overall_pct:.1f}%")

# Which columns have NO missing values
print("\n3c. Columns with ZERO missing values:")
clean_cols = missing_per_col[
    missing_per_col == 0
].index.tolist()
print(f"  {clean_cols}")

# Which columns have missing values
print("\n3d. Columns WITH missing values:")
dirty_cols = missing_per_col[
    missing_per_col > 0
].index.tolist()
for col in dirty_cols:
    count = missing_per_col[col]
    print(f"  {col:<20}: {count} missing")

# ─────────────────────────────────────────────────────
# SECTION 4 - INSPECTING ROWS WITH MISSING DATA
# any(axis=1) checks if ANY value in each row
# is missing
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Rows with Missing Values ---")
print()

# Find rows with at least one missing value
rows_with_missing = df[df.isnull().any(axis=1)]

print(f"4a. Rows with at least one missing value:")
print(f"  Count: {len(rows_with_missing)} rows "
      f"out of {len(df)}\n")
print(rows_with_missing.to_string())

# Count missing values per row
print(f"\n4b. Missing value count per affected row:")
missing_per_row = df.isnull().sum(axis=1)
affected        = missing_per_row[
    missing_per_row > 0
]

for idx, count in affected.items():
    trip = df.loc[idx, 'trip_id']
    cols_missing = df.columns[
        df.iloc[idx].isnull()
    ].tolist()
    print(f"  Row {idx:>2} ({trip}): "
          f"{count} missing — "
          f"{cols_missing}")

# Rows with ALL values present
complete_rows = df[df.notnull().all(axis=1)]
print(f"\n4c. Fully complete rows "
      f"(no missing values):")
print(f"  Count: {len(complete_rows)} rows")
print(complete_rows[
    ['trip_id', 'route_id',
     'delay_minutes', 'status']
].to_string())

# ─────────────────────────────────────────────────────
# SECTION 5 - MISSING VALUE PATTERNS
# Understand WHERE and WHY data is missing
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Missing Value Patterns ---")
print()

print("5a. Missing values by column — severity:")
print()

thresholds = {
    "Critical"  : 20,
    "High"      : 10,
    "Moderate"  : 5,
    "Low"       : 1,
    "None"      : 0,
}

for col in df.columns:
    missing = df[col].isnull().sum()
    pct     = (missing / len(df)) * 100

    if pct >= 20:
        severity = "CRITICAL"
    elif pct >= 10:
        severity = "HIGH"
    elif pct > 0:
        severity = "MODERATE"
    else:
        severity = "CLEAN"

    print(f"  {col:<20}: {missing:>2} missing "
          f"({pct:>4.1f}%) → {severity}")

# Analysis impact
print()
print("5b. Impact on analysis if missing values")
print("    are ignored:")
print()

# What happens to mean if we ignore NaN
mean_with_nan = df['delay_minutes'].mean()
# Manual mean pretending NaN = 0 (wrong approach)
filled_wrong  = df['delay_minutes'].fillna(0)
mean_wrong    = filled_wrong.mean()

print(f"  Correct mean (ignoring NaN automatically):")
print(f"    {mean_with_nan:.2f} minutes")
print(f"  Wrong mean (replacing NaN with 0):")
print(f"    {mean_wrong:.2f} minutes")
print(f"  Difference: "
      f"{abs(mean_with_nan - mean_wrong):.2f} min")
print()
print("  Replacing missing with 0 artificially")
print("  lowers the average — silent error.")
print("  Always detect BEFORE deciding how to handle.")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.33 - Missing Values Detected")
print("=" * 57)