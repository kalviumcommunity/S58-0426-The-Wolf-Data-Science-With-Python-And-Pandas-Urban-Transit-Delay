# inspect_dataframe_transit.py
# Milestone 5.30 - Inspecting DataFrames Using
#                  head(), info(), and describe()
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate the three core DataFrame
#          inspection methods using transit data

import pandas as pd
import numpy as np
import os

print("=" * 57)
print("  MILESTONE 5.30 - INSPECTING DATAFRAMES")
print("  head() | info() | describe()")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Load the transit dataset
# Using the CSV created in Milestone 5.29
# ─────────────────────────────────────────────────────

csv_path = "data/raw/transit_trips.csv"

if not os.path.exists(csv_path):
    print(f"\nCSV not found at {csv_path}")
    print("Creating it now from scratch...")

    # Recreate if missing
    data = {
        "trip_id": [f"T{str(i).zfill(3)}"
                    for i in range(1, 21)],
        "route_id": [
            "Route_42","Route_7","Route_15",
            "Route_23","Route_42","Route_7",
            "Route_15","Route_23","Route_42",
            "Route_7","Route_15","Route_23",
            "Route_42","Route_7","Route_15",
            "Route_23","Route_42","Route_7",
            "Route_15","Route_23"
        ],
        "day_of_week": [
            "Monday","Monday","Monday","Tuesday",
            "Tuesday","Wednesday","Wednesday",
            "Thursday","Thursday","Friday",
            "Friday","Friday","Monday","Tuesday",
            "Wednesday","Thursday","Friday",
            "Monday","Tuesday","Wednesday"
        ],
        "scheduled_departure": [
            "07:00","07:30","08:00","07:15",
            "08:30","07:00","09:00","07:30",
            "08:00","07:15","08:30","09:00",
            "17:00","17:30","18:00","17:15",
            "18:30","08:00","07:45","08:15"
        ],
        "actual_departure": [
            "07:03","07:31","08:01","07:14",
            "08:33","07:08","09:02","07:30",
            "08:09","07:16","08:31","09:00",
            "17:04","17:32","18:01","17:15",
            "18:35","08:02","07:46","08:16"
        ],
        "delay_minutes": [
            17, 31, 4, 0, 22, 34, 3, 2,
            18, 18, 7, 1, 21, 34, 8, 3,
            37, 2, 4, 14
        ],
        "status": [
            "Minor Delay","Severe Delay","On Time",
            "On Time","Major Delay","Severe Delay",
            "On Time","On Time","Major Delay",
            "Major Delay","Minor Delay","On Time",
            "Major Delay","Severe Delay","Minor Delay",
            "On Time","Severe Delay","On Time",
            "On Time","Minor Delay"
        ]
    }
    df = pd.DataFrame(data)
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(csv_path, index=False)
    print(f"CSV created at {csv_path}")
else:
    df = pd.read_csv(csv_path)
    print(f"\nDataset loaded from: {csv_path}")

print(f"Ready to inspect.\n")

# ─────────────────────────────────────────────────────
# SECTION 1 - head() METHOD
# Shows the first N rows of the DataFrame
# Default N = 5
# Use to: visually confirm data loaded correctly,
#         check column alignment, see sample values
# ─────────────────────────────────────────────────────

print("=" * 57)
print("  SECTION 1: head() METHOD")
print("=" * 57)

# Default head() — first 5 rows
print("\n1a. df.head() — default first 5 rows:")
print(df.head().to_string())

print("\nWhat head() tells us:")
print("  Column names visible at the top")
print("  Row index starts at 0 (left column)")
print("  Each row = one trip record")
print("  Sample values confirm data loaded correctly")

# head(3) — custom number
print("\n1b. df.head(3) — first 3 rows only:")
print(df.head(3).to_string())

# head(10) — more rows
print("\n1c. df.head(10) — first 10 rows:")
print(df.head(10).to_string())

# tail() — complement to head()
print("\n1d. df.tail() — last 5 rows:")
print(df.tail().to_string())
print()
print("  tail() confirms the file was read completely")
print("  If last rows look wrong, file may be truncated")

# ─────────────────────────────────────────────────────
# SECTION 2 - info() METHOD
# Shows structural summary of the DataFrame
# Reveals: column names, non-null counts,
#          data types, memory usage
# Use to: check types, find missing values,
#         understand memory footprint
# ─────────────────────────────────────────────────────

print("\n" + "=" * 57)
print("  SECTION 2: info() METHOD")
print("=" * 57)

print("\n2a. df.info() — full structural summary:")
print()
df.info()

print("\nWhat info() tells us:")
print(f"  RangeIndex     : {len(df)} entries (0 to "
      f"{len(df)-1})")
print(f"  Total columns  : {len(df.columns)}")
print()

# Explain each column type found
print("Column type breakdown:")
for col in df.columns:
    dtype   = df[col].dtype
    nulls   = df[col].isnull().sum()
    unique  = df[col].nunique()
    print(f"  {col:<25} dtype={str(dtype):<8} "
          f"nulls={nulls}  unique={unique}")

print()
print("Data type guide:")
print("  object  → text/string data "
      "(route names, status labels)")
print("  int64   → integer numbers "
      "(delay_minutes, counts)")
print("  float64 → decimal numbers "
      "(percentages, averages)")
print("  bool    → True/False values")

# info() on specific dtypes
print("\n2b. Numeric columns only:")
numeric_cols = df.select_dtypes(
    include=['int64', 'float64']
)
print(f"  Numeric columns: "
      f"{list(numeric_cols.columns)}")

print("\n2c. Object (text) columns only:")
text_cols = df.select_dtypes(include=['object'])
print(f"  Text columns   : "
      f"{list(text_cols.columns)}")

# ─────────────────────────────────────────────────────
# SECTION 3 - describe() METHOD
# Generates statistical summary of numeric columns
# Reveals: count, mean, std, min, max, percentiles
# Use to: understand distributions, spot outliers,
#         validate numeric ranges
# ─────────────────────────────────────────────────────

print("\n" + "=" * 57)
print("  SECTION 3: describe() METHOD")
print("=" * 57)

# Default describe — numeric columns only
print("\n3a. df.describe() — numeric summary:")
print(df.describe().to_string())

print("\nWhat each row means for delay_minutes:")
desc = df['delay_minutes'].describe()
print(f"  count  = {desc['count']:.0f}   "
      f"→ number of non-null values")
print(f"  mean   = {desc['mean']:.2f}  "
      f"→ average delay across all trips")
print(f"  std    = {desc['std']:.2f}  "
      f"→ how spread out delays are")
print(f"  min    = {desc['min']:.0f}    "
      f"→ shortest delay (best case)")
print(f"  25%    = {desc['25%']:.2f}   "
      f"→ 25% of trips delayed less than this")
print(f"  50%    = {desc['50%']:.2f}   "
      f"→ median delay (middle value)")
print(f"  75%    = {desc['75%']:.2f}  "
      f"→ 75% of trips delayed less than this")
print(f"  max    = {desc['max']:.0f}   "
      f"→ longest delay (worst case)")

# describe() on single column
print("\n3b. df['delay_minutes'].describe():")
print(df['delay_minutes'].describe().to_string())

# describe() including text columns
print("\n3c. df.describe(include='all') — all columns:")
print(df.describe(include='all').to_string())

print()
print("For text columns describe() shows:")
print("  count  → non-null entries")
print("  unique → distinct values")
print("  top    → most frequent value")
print("  freq   → how often top value appears")

# ─────────────────────────────────────────────────────
# SECTION 4 - COMBINING ALL THREE METHODS
# The standard inspection routine before any analysis
# ─────────────────────────────────────────────────────

print("\n" + "=" * 57)
print("  SECTION 4: Standard Inspection Routine")
print("=" * 57)

print()
print("Every dataset should be inspected with")
print("this 3-step routine before any analysis:\n")

print("STEP 1 — df.head() answers:")
print("  'Does the data look right?'")
print("  'Are column names correct?'")
print("  'Are sample values sensible?'")
print()

print("STEP 2 — df.info() answers:")
print("  'How many rows and columns?'")
print("  'What type is each column?'")
print("  'Are there any missing values?'")
print()

print("STEP 3 — df.describe() answers:")
print("  'What are the numeric ranges?'")
print("  'What is the average value?'")
print("  'Are there potential outliers?'")
print()

# Practical findings from this dataset
print("Findings from inspecting transit_trips.csv:")
print()

avg_delay   = df['delay_minutes'].mean()
max_delay   = df['delay_minutes'].max()
null_count  = df.isnull().sum().sum()
n_routes    = df['route_id'].nunique()
top_status  = df['status'].value_counts().index[0]
top_route   = df['route_id'].value_counts().index[0]

print(f"  Rows              : {len(df)}")
print(f"  Columns           : {len(df.columns)}")
print(f"  Missing values    : {null_count} "
      f"← safe to proceed")
print(f"  Unique routes     : {n_routes}")
print(f"  Average delay     : {avg_delay:.1f} min")
print(f"  Max delay         : {max_delay} min "
      f"← potential outlier to check")
print(f"  Most common status: {top_status}")
print(f"  Most trips        : {top_route}")

# ─────────────────────────────────────────────────────
# SECTION 5 - WHEN INSPECTION CATCHES PROBLEMS
# Simulate a bad dataset and show what inspection
# reveals before analysis starts
# ─────────────────────────────────────────────────────

print("\n" + "=" * 57)
print("  SECTION 5: Inspection Catching Issues")
print("=" * 57)
print()

# Create a dataset with common problems
bad_data = pd.DataFrame({
    "trip_id"      : ["T001", "T002", "T003",
                      "T004", "T005"],
    "route_id"     : ["Route_42", None, "Route_15",
                      "Route_7", "Route_23"],
    "delay_minutes": [14, 22, None, -5, 999],
    "status"       : ["Minor Delay", "Major Delay",
                      "On Time", "On Time",
                      "Severe Delay"]
})

print("Inspecting a problematic dataset:\n")

print("head() preview:")
print(bad_data.head().to_string())

print("\ninfo() reveals:")
bad_data.info()

print("\ndescribe() reveals:")
print(bad_data.describe().to_string())

print()
print("Issues inspection caught:")
print("  route_id null   : 1 missing value found "
      "in info()")
print("  delay null      : 1 missing value found "
      "in info()")
print("  delay min = -5  : impossible value "
      "seen in describe()")
print("  delay max = 999 : extreme outlier "
      "seen in describe()")
print()
print("Without inspection these would cause")
print("silent errors in analysis downstream.")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.30 - Inspection Methods Verified")
print("=" * 57)