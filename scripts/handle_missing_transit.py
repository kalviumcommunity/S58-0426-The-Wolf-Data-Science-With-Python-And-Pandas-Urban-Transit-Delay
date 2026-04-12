# handle_missing_transit.py
# Milestone 5.34 - Handling Missing Values Using
#                  Drop and Fill Strategies
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate dropna, fillna, and
#          strategy selection for missing data
#          using transit domain examples

import pandas as pd
import numpy as np

print("=" * 57)
print("  MILESTONE 5.34 - HANDLING MISSING VALUES")
print("  Drop and Fill Strategies")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Create transit dataset with missing values
# Same structure as Milestone 5.33 — detection done,
# now we handle what we found
# ─────────────────────────────────────────────────────

print("\n--- SETUP: Loading Dataset with Missing Values---")
print()

data = {
    "trip_id": [
        "T001","T002","T003","T004","T005",
        "T006","T007","T008","T009","T010",
        "T011","T012","T013","T014","T015",
        "T016","T017","T018","T019","T020"
    ],
    "route_id": [
        "Route_42","Route_7", None,      "Route_23",
        "Route_42","Route_7", None,      "Route_23",
        "Route_42","Route_7", "Route_15","Route_23",
        "Route_42", None,    "Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23"
    ],
    "day_of_week": [
        "Monday","Monday","Tuesday","Tuesday",
        "Wednesday","Wednesday","Thursday","Thursday",
        "Friday","Friday","Monday","Tuesday",
        "Wednesday","Thursday","Friday","Monday",
        "Tuesday","Wednesday","Thursday","Friday"
    ],
    "hour_of_day": [
        8, 9, 7, 8, 17, 18, 8, 7,
        9, 17, 8, 18, 7, None, 8,    # T014 missing
        17, None, 8, 7, 9             # T017 missing
    ],
    "delay_minutes": [
        14, 31,  5,  0, 22,
        34,  3,  2, 18, 18,
        None, 1, 21, 34, None,        # T011,T015 missing
        3,  37,  2,  4, 14
    ],
    "status": [
        "Minor Delay", "Severe Delay","On Time",
        "On Time",     "Major Delay", "Severe Delay",
        "On Time",     "On Time",     "Major Delay",
        "Major Delay", None,          "On Time",
        "Major Delay", "Severe Delay", None,
        "On Time",     "Severe Delay","On Time",
        "On Time",     "Minor Delay"
    ],
    "passenger_count": [
        42,  None, 38,  55,  61,      # T002 missing
        None, 29,  44,  None, 57,     # T006,T009 missing
        33,  48,  None, 62,  41,      # T013 missing
        None, 39,  52,  47,  None     # T016,T020 missing
    ]
}

df_original = pd.DataFrame(data)

# Quick missing value summary
print("Dataset shape        : "
      f"{df_original.shape}")
print("Missing per column:")
for col in df_original.columns:
    n = df_original[col].isnull().sum()
    if n > 0:
        pct = n / len(df_original) * 100
        print(f"  {col:<20}: "
              f"{n} missing ({pct:.0f}%)")

total_missing = df_original.isnull().sum().sum()
print(f"\nTotal missing cells  : {total_missing}")
print(f"Rows                 : {len(df_original)}")

# ─────────────────────────────────────────────────────
# SECTION 1 - DROP STRATEGIES
# dropna() removes rows or columns with NaN
# Use when: missing data is few and random,
#           or when the row is critical to be complete
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Drop Strategies ---")
print()

# 1a — Drop ANY row with at least one missing value
df_drop_any = df_original.dropna()
print("1a. dropna() — drop rows with ANY missing:")
print(f"  Before: {len(df_original)} rows")
print(f"  After : {len(df_drop_any)} rows")
print(f"  Lost  : "
      f"{len(df_original) - len(df_drop_any)} rows")
print(f"  Data retained: "
      f"{len(df_drop_any)/len(df_original)*100:.0f}%")
print()
print("  Dropped trip IDs:")
dropped_ids = set(df_original['trip_id']) - \
              set(df_drop_any['trip_id'])
print(f"  {sorted(dropped_ids)}")

# 1b — Drop rows missing in SPECIFIC columns only
# Only drop if delay_minutes or route_id is missing
# because these are critical for analysis
df_drop_key = df_original.dropna(
    subset=['delay_minutes', 'route_id']
)
print("1b. dropna(subset=['delay_minutes','route_id'])")
print(f"  Before: {len(df_original)} rows")
print(f"  After : {len(df_drop_key)} rows")
print(f"  Lost  : "
      f"{len(df_original)-len(df_drop_key)} rows")
print(f"  Data retained: "
      f"{len(df_drop_key)/len(df_original)*100:.0f}%")
print()
print("  WHY: delay_minutes and route_id are the core")
print("  analysis columns. Trips missing these cannot")
print("  contribute to delay calculations at all.")

# 1c — Drop columns with high missing percentage
threshold_pct = 25
print(f"\n1c. Drop columns with >{threshold_pct}% "
      f"missing:")
missing_pct = (df_original.isnull().sum() /
               len(df_original) * 100)
cols_to_drop = missing_pct[
    missing_pct > threshold_pct
].index.tolist()

print(f"  Columns to drop: {cols_to_drop}")
df_drop_cols = df_original.drop(
    columns=cols_to_drop
)
print(f"  Before: {df_original.shape[1]} columns")
print(f"  After : {df_drop_cols.shape[1]} columns")

# 1d — thresh parameter — keep rows with minimum
# number of non-null values
min_non_null = 5
df_thresh = df_original.dropna(thresh=min_non_null)
print(f"\n1d. dropna(thresh={min_non_null}) — keep rows "
      f"with at least {min_non_null} non-null values:")
print(f"  Before: {len(df_original)} rows")
print(f"  After : {len(df_thresh)} rows")

# ─────────────────────────────────────────────────────
# SECTION 2 - FILL STRATEGIES
# fillna() replaces NaN with a specified value
# Use when: dropping would lose too much data,
#           or a sensible substitute exists
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Fill Strategies ---")
print()

# Always work on a COPY — never modify original
df_filled = df_original.copy()

# 2a — Fill with CONSTANT value
print("2a. Fill with constant — "
      "hour_of_day with 0:")
before_nulls = df_filled['hour_of_day'].isnull().sum()
df_filled['hour_of_day'] = \
    df_filled['hour_of_day'].fillna(0)
after_nulls = df_filled['hour_of_day'].isnull().sum()
print(f"  Before: {before_nulls} missing")
print(f"  After : {after_nulls} missing")
print(f"  Note  : filling with 0 means 'unknown hour'")
print(f"  This is only acceptable if 0 is not a valid")
print(f"  hour in the analysis (midnight trips absent)")

# Reset for next demo
df_filled = df_original.copy()

# 2b — Fill with MEAN (numeric columns)
mean_delay = df_filled['delay_minutes'].mean()
print(f"\n2b. Fill with MEAN — delay_minutes:")
print(f"  Mean delay (excluding NaN): "
      f"{mean_delay:.2f} min")
before = df_filled['delay_minutes'].isnull().sum()
df_filled['delay_minutes'] = \
    df_filled['delay_minutes'].fillna(mean_delay)
after = df_filled['delay_minutes'].isnull().sum()
print(f"  Before: {before} missing")
print(f"  After : {after} missing")
print(f"  Missing values filled with {mean_delay:.2f}")
print(f"  WHY mean: neutral fill — does not pull")
print(f"  average up or down significantly")

# 2c — Fill with MEDIAN (better for skewed data)
df_filled2 = df_original.copy()
median_delay = df_filled2['delay_minutes'].median()
print(f"\n2c. Fill with MEDIAN — delay_minutes:")
print(f"  Median delay               : "
      f"{median_delay:.1f} min")
df_filled2['delay_minutes'] = \
    df_filled2['delay_minutes'].fillna(median_delay)
print(f"  Missing values filled with {median_delay:.1f}")
print(f"  WHY median: better than mean when data is")
print(f"  skewed — extreme delays do not affect it")

# Compare mean vs median fill effect
print(f"\n  Comparison — delay_minutes after filling:")
print(f"  Original mean (with NaN skipped): "
      f"{df_original['delay_minutes'].mean():.2f}")
print(f"  After mean fill  : "
      f"{df_filled['delay_minutes'].mean():.2f}")
print(f"  After median fill: "
      f"{df_filled2['delay_minutes'].mean():.2f}")

# 2d — Fill with MODE (for categorical columns)
df_filled3 = df_original.copy()
mode_status = df_filled3['status'].mode()[0]
print(f"\n2d. Fill with MODE — status (categorical):")
print(f"  Most common status: '{mode_status}'")
before = df_filled3['status'].isnull().sum()
df_filled3['status'] = \
    df_filled3['status'].fillna(mode_status)
after = df_filled3['status'].isnull().sum()
print(f"  Before: {before} missing")
print(f"  After : {after} missing")
print(f"  WHY mode: for text/category columns mean")
print(f"  and median do not apply — most frequent")
print(f"  value is the safest neutral choice")

# 2e — Fill with FORWARD FILL (ffill)
df_filled4 = df_original.copy()
print(f"\n2e. Forward fill (ffill) — route_id:")
print(f"  Before:")
print(df_filled4[['trip_id', 'route_id']
                  ].head(8).to_string())
df_filled4['route_id'] = \
    df_filled4['route_id'].ffill()
print(f"\n  After ffill:")
print(df_filled4[['trip_id', 'route_id']
                  ].head(8).to_string())
print(f"\n  WHY ffill: propagates last known value")
print(f"  forward. Works when consecutive records")
print(f"  on the same route are likely the same")
print(f"  CAUTION: only valid with ordered time data")

# ─────────────────────────────────────────────────────
# SECTION 3 - CHOOSING DROP vs FILL
# Decision framework based on context
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Drop vs Fill Decision ---")
print()
print("Decision framework for each column:\n")

decisions = [
    ("trip_id",
     "0%", "0", "N/A — no missing values",
     "KEEP AS IS"),
    ("route_id",
     "15%", "Low",
     "Core analysis column — use ffill or mode",
     "FILL with ffill"),
    ("day_of_week",
     "0%", "0", "N/A — no missing values",
     "KEEP AS IS"),
    ("hour_of_day",
     "10%", "Low",
     "Important for peak analysis — fill with median",
     "FILL with median"),
    ("delay_minutes",
     "10%", "Critical",
     "Core metric — fill with median not mean",
     "FILL with median"),
    ("status",
     "10%", "Medium",
     "Categorical — fill with mode",
     "FILL with mode"),
    ("passenger_count",
     "30%", "High",
     "Supporting column — fill with median or drop",
     "FILL with median"),
]

print(f"  {'Column':<20} {'Missing':<9} "
      f"{'Priority':<10} Strategy")
print("  " + "-" * 60)
for col, pct, pri, reason, strategy in decisions:
    print(f"  {col:<20} {pct:<9} "
          f"{pri:<10} {strategy}")

print()
print("Reasoning behind each decision:")
for col, pct, pri, reason, strategy in decisions:
    if pct != "0%":
        print(f"  {col}: {reason}")

# ─────────────────────────────────────────────────────
# SECTION 4 - APPLYING THE FULL CLEANING STRATEGY
# Apply all decisions in one clean pipeline
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Complete Cleaning Pipeline ---")
print()

# Start from original
df_clean = df_original.copy()

print(f"Before cleaning:")
print(f"  Shape          : {df_clean.shape}")
print(f"  Missing values : "
      f"{df_clean.isnull().sum().sum()}")
print()

# Step 1 — Drop rows missing critical columns
df_clean = df_clean.dropna(
    subset=['delay_minutes', 'route_id']
)
print(f"After dropping rows missing delay/route:")
print(f"  Rows remaining : {len(df_clean)}")

# Step 2 — Fill hour_of_day with median
median_hour = df_clean['hour_of_day'].median()
df_clean['hour_of_day'] = \
    df_clean['hour_of_day'].fillna(median_hour)
print(f"\nAfter filling hour_of_day with median "
      f"({median_hour:.0f}):")
print(f"  hour_of_day nulls: "
      f"{df_clean['hour_of_day'].isnull().sum()}")

# Step 3 — Fill status with mode
mode_status = df_clean['status'].mode()[0]
df_clean['status'] = \
    df_clean['status'].fillna(mode_status)
print(f"\nAfter filling status with mode "
      f"('{mode_status}'):")
print(f"  status nulls   : "
      f"{df_clean['status'].isnull().sum()}")

# Step 4 — Fill passenger_count with median
median_pax = df_clean['passenger_count'].median()
df_clean['passenger_count'] = \
    df_clean['passenger_count'].fillna(median_pax)
print(f"\nAfter filling passenger_count with median "
      f"({median_pax:.0f}):")
print(f"  passenger nulls: "
      f"{df_clean['passenger_count'].isnull().sum()}")

# Final state
print(f"\nFinal cleaned dataset:")
print(f"  Shape          : {df_clean.shape}")
print(f"  Missing values : "
      f"{df_clean.isnull().sum().sum()}")
print(f"  Rows retained  : {len(df_clean)} of "
      f"{len(df_original)} original")
print(f"  Data retained  : "
      f"{len(df_clean)/len(df_original)*100:.0f}%")

print("\nFinal DataFrame:")
print(df_clean.to_string())

# Save cleaned data to processed folder
import os
os.makedirs("data/processed", exist_ok=True)
df_clean.to_csv(
    "data/processed/transit_trips_clean.csv",
    index=False
)
print(f"\nCleaned data saved to: "
      f"data/processed/transit_trips_clean.csv")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.34 - Missing Values Handled")
print("=" * 57)