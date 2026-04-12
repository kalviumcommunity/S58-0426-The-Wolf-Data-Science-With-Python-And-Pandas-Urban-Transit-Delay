# indexing_slicing_transit.py
# Milestone 5.32 - Selecting Rows and Columns
#                  Using Indexing and Slicing
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate column selection, iloc,
#          loc, boolean filtering, and combined
#          selection using transit data

import pandas as pd
import numpy as np

print("=" * 57)
print("  MILESTONE 5.32 - INDEXING AND SLICING")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Create standardized transit dataset
# ─────────────────────────────────────────────────────

print("\n--- SETUP: Transit Dataset ---\n")

data = {
    "trip_id": [
        "T001","T002","T003","T004","T005",
        "T006","T007","T008","T009","T010",
        "T011","T012","T013","T014","T015"
    ],
    "route_id": [
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15"
    ],
    "day_of_week": [
        "Monday","Monday","Tuesday","Tuesday",
        "Wednesday","Wednesday","Thursday","Thursday",
        "Friday","Friday","Monday","Tuesday",
        "Wednesday","Thursday","Friday"
    ],
    "hour_of_day": [
        8, 9, 7, 8, 17, 18, 8, 7,
        9, 17, 8, 18, 7, 9, 8
    ],
    "delay_minutes": [
        14, 31, 5, 0, 22, 34, 3, 2,
        18, 18, 7, 1, 21, 34, 8
    ],
    "passenger_count": [
        42, 58, 38, 55, 61, 67, 29, 44,
        57, 63, 33, 48, 52, 62, 41
    ],
    "status": [
        "Minor Delay","Severe Delay","On Time",
        "On Time","Major Delay","Severe Delay",
        "On Time","On Time","Major Delay",
        "Major Delay","Minor Delay","On Time",
        "Major Delay","Severe Delay","Minor Delay"
    ],
    "is_peak_hour": [
        True, True, True, True, True, True,
        True, True, True, True, True, False,
        True, True, True
    ]
}

df = pd.DataFrame(data)

# Set trip_id as the index for loc demonstrations
df = df.set_index("trip_id")

print(f"Dataset shape        : {df.shape}")
print(f"Index (trip_id)      : "
      f"{list(df.index[:5])} ...")
print(f"Columns              : {list(df.columns)}")
print(f"\nFull dataset:")
print(df.to_string())

# ─────────────────────────────────────────────────────
# SECTION 1 - SELECTING COLUMNS BY NAME
# Single column  → returns a Series
# Multiple cols  → returns a DataFrame
# Use [] notation for column selection
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Selecting Columns ---")
print()

# 1a — Single column → Series
print("1a. Single column — df['delay_minutes']:")
single_col = df['delay_minutes']
print(f"  Type   : {type(single_col).__name__}")
print(f"  Values : {single_col.values}")
print(f"  dtype  : {single_col.dtype}")

# 1b — Multiple columns → DataFrame
print("\n1b. Multiple columns — "
      "df[['route_id','delay_minutes','status']]:")
multi_col = df[['route_id',
                'delay_minutes',
                'status']]
print(f"  Type   : {type(multi_col).__name__}")
print(f"  Shape  : {multi_col.shape}")
print(multi_col.to_string())

# 1c — All numeric columns
print("\n1c. Numeric columns only:")
numeric_df = df.select_dtypes(
    include=['int64','float64','bool']
)
print(f"  Columns: {list(numeric_df.columns)}")
print(numeric_df.head(3).to_string())

# 1d — Practical use — select analysis columns
print("\n1d. Analysis subset — "
      "route + hour + delay:")
analysis_cols = df[['route_id',
                     'hour_of_day',
                     'delay_minutes']]
print(analysis_cols.to_string())

# ─────────────────────────────────────────────────────
# SECTION 2 - SELECTING ROWS BY POSITION (iloc)
# iloc = integer location
# Uses ZERO-BASED integer positions
# Works like Python list slicing
# Syntax: df.iloc[row_pos, col_pos]
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: iloc — Position-Based ---")
print()
print("iloc uses integer positions (0-based)")
print("Works like list slicing: start:stop:step\n")

# 2a — Single row by position
print("2a. Single row — df.iloc[0]:")
print(df.iloc[0].to_string())

# 2b — Multiple specific rows
print("\n2b. Rows 0, 2, 4 — df.iloc[[0,2,4]]:")
print(df.iloc[[0, 2, 4]].to_string())

# 2c — Row range (slice)
print("\n2c. First 5 rows — df.iloc[:5]:")
print(df.iloc[:5].to_string())

# 2d — Last 3 rows
print("\n2d. Last 3 rows — df.iloc[-3:]:")
print(df.iloc[-3:].to_string())

# 2e — Rows and columns by position
print("\n2e. Rows 0-4, columns 0-2 — "
      "df.iloc[:5, :3]:")
print(df.iloc[:5, :3].to_string())

# 2f — Specific row and column
print("\n2f. Row 2, column 3 — df.iloc[2, 3]:")
val = df.iloc[2, 3]
print(f"  Value : {val}")
print(f"  This is row index 2, column index 3")
print(f"  = trip T003, delay_minutes")

# 2g — Every other row
print("\n2g. Every other row — df.iloc[::2]:")
print(df.iloc[::2][['route_id',
                     'delay_minutes']].to_string())

# ─────────────────────────────────────────────────────
# SECTION 3 - SELECTING ROWS BY LABEL (loc)
# loc = label-based indexing
# Uses the actual INDEX VALUES (trip_id here)
# Also uses actual COLUMN NAMES
# Syntax: df.loc[row_label, col_name]
# IMPORTANT: loc is inclusive on both ends
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: loc — Label-Based ---")
print()
print("loc uses actual index labels and column names")
print("Both endpoints are INCLUSIVE in slices\n")

# 3a — Single row by label
print("3a. Single row — df.loc['T001']:")
print(df.loc['T001'].to_string())

# 3b — Multiple specific rows by label
print("\n3b. Specific rows — "
      "df.loc[['T001','T005','T010']]:")
print(df.loc[['T001','T005','T010']].to_string())

# 3c — Range of rows by label (INCLUSIVE)
print("\n3c. Label range T003 to T007 — "
      "df.loc['T003':'T007']:")
print(df.loc['T003':'T007'].to_string())
print("  Note: T007 IS included (loc is inclusive)")

# 3d — Row + specific columns by name
print("\n3d. Specific row and columns — "
      "df.loc['T001', ['route_id','delay_minutes']]:")
print(df.loc['T001',
             ['route_id', 'delay_minutes']])

# 3e — Range of rows + range of columns
print("\n3e. Rows T001-T005, "
      "cols route_id to delay_minutes:")
print(df.loc['T001':'T005',
             'route_id':'delay_minutes'].to_string())

# 3f — Single cell
print("\n3f. Single cell — "
      "df.loc['T006', 'delay_minutes']:")
cell = df.loc['T006', 'delay_minutes']
print(f"  Value: {cell} minutes")

# ─────────────────────────────────────────────────────
# SECTION 4 - BOOLEAN FILTERING
# Select rows based on conditions
# Returns only rows where condition is True
# Most common selection method in real analysis
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Boolean Filtering ---")
print()

# 4a — Single condition
print("4a. Trips with delay > 20 minutes:")
mask_delay = df['delay_minutes'] > 20
filtered   = df[mask_delay]
print(f"  Rows matching: {len(filtered)}")
print(filtered[['route_id',
                 'delay_minutes',
                 'status']].to_string())

# 4b — Single condition — specific route
print("\n4b. Route_42 trips only:")
route_mask = df['route_id'] == 'Route_42'
route_df   = df[route_mask]
print(route_df[['route_id',
                 'delay_minutes',
                 'status']].to_string())

# 4c — AND condition (both must be True)
print("\n4c. Peak hour AND delay > 15 (AND):")
peak_and_delay = (df['is_peak_hour'] == True) & \
                 (df['delay_minutes'] > 15)
result_and     = df[peak_and_delay]
print(f"  Rows matching: {len(result_and)}")
print(result_and[['route_id',
                   'hour_of_day',
                   'delay_minutes',
                   'status']].to_string())

# 4d — OR condition (either can be True)
print("\n4d. Route_7 OR severe delay (OR):")
or_mask   = (df['route_id'] == 'Route_7') | \
            (df['status']   == 'Severe Delay')
result_or = df[or_mask]
print(f"  Rows matching: {len(result_or)}")
print(result_or[['route_id',
                  'delay_minutes',
                  'status']].to_string())

# 4e — isin() — match multiple values
print("\n4e. Monday or Friday trips (isin):")
day_mask = df['day_of_week'].isin(
    ['Monday', 'Friday']
)
print(df[day_mask][['route_id',
                     'day_of_week',
                     'delay_minutes']].to_string())

# ─────────────────────────────────────────────────────
# SECTION 5 - COMBINING ROW AND COLUMN SELECTION
# Use loc with boolean mask + column list
# Most powerful and common pattern
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Combined Row + Column ---")
print()

# 5a — Boolean filter + column selection
print("5a. Severe delays — route and delay only:")
severe_mask = df['status'] == 'Severe Delay'
result_5a   = df.loc[severe_mask,
                      ['route_id',
                       'delay_minutes',
                       'is_peak_hour']]
print(result_5a.to_string())

# 5b — Peak hour Route_42 analysis
print("\n5b. Peak hour Route_42 full profile:")
peak_42 = (df['route_id']     == 'Route_42') & \
          (df['is_peak_hour'] == True)
result_5b = df.loc[peak_42,
                    ['route_id',
                     'hour_of_day',
                     'delay_minutes',
                     'passenger_count',
                     'status']]
print(result_5b.to_string())
print(f"\n  Average delay on peak Route_42: "
      f"{result_5b['delay_minutes'].mean():.1f} min")
print(f"  Total passengers affected     : "
      f"{result_5b['passenger_count'].sum()}")

# 5c — iloc vs loc comparison
print("\n5c. iloc vs loc — same result different way:")
print("  iloc[:3, :2] — first 3 rows, first 2 cols:")
print(df.iloc[:3, :2].to_string())
print("\n  loc['T001':'T003', "
      "['route_id','day_of_week']]:")
print(df.loc['T001':'T003',
             ['route_id', 'day_of_week']].to_string())
print("\n  Both return same rows and columns")
print("  iloc: use when you know position numbers")
print("  loc : use when you know labels and names")

# ─────────────────────────────────────────────────────
# SECTION 6 - SELECTION REFERENCE SUMMARY
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Selection Reference ---")
print()
print(f"  {'Method':<30} Description")
print("  " + "-" * 55)
methods = [
    ("df['col']",
     "Single column → Series"),
    ("df[['col1','col2']]",
     "Multiple columns → DataFrame"),
    ("df.iloc[n]",
     "Row by integer position"),
    ("df.iloc[a:b]",
     "Row slice by position (b excluded)"),
    ("df.iloc[r, c]",
     "Cell by row+col position"),
    ("df.loc['label']",
     "Row by index label"),
    ("df.loc['a':'b']",
     "Row slice by label (b INCLUDED)"),
    ("df.loc['label', 'col']",
     "Cell by label+column name"),
    ("df[df['col'] > val]",
     "Boolean row filter"),
    ("df.loc[mask, ['c1','c2']]",
     "Boolean filter + columns"),
]
for method, desc in methods:
    print(f"  {method:<30} {desc}")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.32 - Indexing Verified")
print("=" * 57)