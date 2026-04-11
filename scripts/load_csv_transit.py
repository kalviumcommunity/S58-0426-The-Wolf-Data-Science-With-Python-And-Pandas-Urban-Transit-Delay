# load_csv_transit.py
# Milestone 5.29 - Loading CSV Data into Pandas DataFrames
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate loading, inspecting, and
#          verifying CSV data using Pandas

import pandas as pd
import os

print("=" * 57)
print("  MILESTONE 5.29 - LOADING CSV INTO DATAFRAME")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - UNDERSTANDING THE CSV FILE
# Before loading, always know what the file contains
# CSV = Comma Separated Values
# Row 1 = header (column names)
# Rows 2+ = data records
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Understanding the CSV File ---")
print()

csv_path = "data/raw/transit_trips.csv"

# Verify the file exists before loading
if os.path.exists(csv_path):
    file_size = os.path.getsize(csv_path)
    print(f"File path            : {csv_path}")
    print(f"File exists          : True")
    print(f"File size            : {file_size} bytes")
else:
    print(f"ERROR: File not found at {csv_path}")
    print("Please ensure transit_trips.csv is in "
          "data/raw/ folder")
    exit()

# Preview raw file content — first 3 lines
print(f"\nRaw CSV preview (first 3 lines):")
with open(csv_path, "r") as f:
    for i, line in enumerate(f):
        if i < 3:
            print(f"  Line {i+1}: {line.strip()}")
        else:
            break

print()
print("Structure explanation:")
print("  Line 1  → header row (column names)")
print("  Line 2+ → data rows (one trip per row)")
print("  Comma   → delimiter separating values")

# ─────────────────────────────────────────────────────
# SECTION 2 - LOADING CSV INTO PANDAS DATAFRAME
# pd.read_csv() is the standard loading function
# It automatically detects headers and data types
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Loading CSV with pd.read_csv ---")
print()

# Basic load
df = pd.read_csv(csv_path)

print(f"pd.read_csv('{csv_path}') completed")
print(f"Type of result       : {type(df)}")
print(f"Rows loaded          : {len(df)}")
print(f"Columns loaded       : {len(df.columns)}")
print(f"\nColumn names:")
for i, col in enumerate(df.columns):
    print(f"  [{i}] {col}")

# ─────────────────────────────────────────────────────
# SECTION 3 - INSPECTING LOADED DATA
# Always inspect immediately after loading
# Never assume the data loaded correctly
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Inspecting Loaded Data ---")

# head() — first 5 rows
print("\n3a. df.head() — first 5 rows:")
print(df.head().to_string(index=True))

# tail() — last 5 rows
print("\n3b. df.tail() — last 5 rows:")
print(df.tail().to_string(index=True))

# shape — rows and columns count
print(f"\n3c. df.shape:")
print(f"  {df.shape} → "
      f"{df.shape[0]} rows, "
      f"{df.shape[1]} columns")

# dtypes — data type of each column
print(f"\n3d. df.dtypes — column data types:")
for col, dtype in df.dtypes.items():
    print(f"  {col:<25}: {dtype}")

# info() — full structural summary
print(f"\n3e. df.info():")
df.info()

# ─────────────────────────────────────────────────────
# SECTION 4 - ACCESSING COLUMNS AND ROWS
# After loading, access data by column name or index
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Accessing Columns and Rows ---")
print()

# Access single column
print("4a. Single column access — df['route_id']:")
print(f"  {df['route_id'].values}")

# Access multiple columns
print("\n4b. Multiple columns — "
      "df[['trip_id','route_id','delay_minutes']]:")
subset = df[['trip_id', 'route_id', 'delay_minutes']]
print(subset.head(5).to_string(index=True))

# Access specific row by index
print("\n4c. Single row — df.iloc[0]:")
print(df.iloc[0].to_string())

# Access specific cell
print(f"\n4d. Single cell — "
      f"df.iloc[0]['delay_minutes']:")
print(f"  Value: {df.iloc[0]['delay_minutes']} minutes")

# ─────────────────────────────────────────────────────
# SECTION 5 - BASIC DATA VERIFICATION
# Verify the loaded data matches expectations
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Data Verification ---")
print()

# Expected values to verify against
expected_rows   = 20
expected_cols   = 9
expected_routes = ["Route_7", "Route_15",
                   "Route_42", "Route_23"]

# Row count check
row_check = len(df) == expected_rows
print(f"Row count check:")
print(f"  Expected : {expected_rows}")
print(f"  Loaded   : {len(df)}")
print(f"  Passed   : {row_check}")

# Column count check
col_check = len(df.columns) == expected_cols
print(f"\nColumn count check:")
print(f"  Expected : {expected_cols}")
print(f"  Loaded   : {len(df.columns)}")
print(f"  Passed   : {col_check}")

# Unique routes check
loaded_routes = sorted(df['route_id'].unique())
route_check   = loaded_routes == \
                sorted(expected_routes)
print(f"\nRoute ID check:")
print(f"  Expected : {sorted(expected_routes)}")
print(f"  Loaded   : {loaded_routes}")
print(f"  Passed   : {route_check}")

# Missing values check
missing = df.isnull().sum().sum()
print(f"\nMissing values check:")
print(f"  Total missing values: {missing}")
print(f"  Passed   : {missing == 0}")

# Delay range check
min_d  = df['delay_minutes'].min()
max_d  = df['delay_minutes'].max()
print(f"\nDelay range check:")
print(f"  Min delay: {min_d} minutes")
print(f"  Max delay: {max_d} minutes")
print(f"  Range    : {min_d} to {max_d} minutes")

# ─────────────────────────────────────────────────────
# SECTION 6 - COMMON LOADING ISSUES DEMONSTRATED
# Show what goes wrong with incorrect loading
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Common Loading Issues ---")
print()

# Issue 1 — wrong file path
print("Issue 1: Wrong file path")
try:
    df_bad = pd.read_csv("data/raw/wrong_name.csv")
except FileNotFoundError as e:
    print(f"  FileNotFoundError caught")
    print(f"  Fix: verify path with os.path.exists()")

# Issue 2 — skiprows used incorrectly
print("\nIssue 2: skiprows skipping the header")
df_skip = pd.read_csv(csv_path, skiprows=1,
                       header=None)
print(f"  Columns become: {list(df_skip.columns[:4])}")
print(f"  First row     : "
      f"{df_skip.iloc[0, 0]} ← was data, not header")
print(f"  Fix: do not use skiprows unless you know")
print(f"  the file has non-data rows at the top")

# Issue 3 — loading with wrong separator
print("\nIssue 3: Specifying wrong separator")
df_sep = pd.read_csv(csv_path, sep=";")
print(f"  Column count  : {len(df_sep.columns)} "
      f"(expected 9, got {len(df_sep.columns)})")
print(f"  First column  : {df_sep.columns[0]}")
print(f"  Fix: CSV uses comma by default — "
      f"only change sep if file uses another delimiter")

# ─────────────────────────────────────────────────────
# SECTION 7 - QUICK SUMMARY STATS FROM LOADED DATA
# Immediate value from pd.read_csv + describe()
# ─────────────────────────────────────────────────────

print("\n--- SECTION 7: Quick Summary from Loaded Data---")
print()

print("df['delay_minutes'].describe():")
print(df['delay_minutes'].describe().to_string())

print("\nTrips per route:")
print(df['route_id'].value_counts().to_string())

print("\nStatus distribution:")
print(df['status'].value_counts().to_string())

print("\nAverage delay per route:")
avg_per_route = df.groupby('route_id')[
    'delay_minutes'].mean().round(1)
print(avg_per_route.to_string())

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.29 - CSV Loading Verified")
print("=" * 57)