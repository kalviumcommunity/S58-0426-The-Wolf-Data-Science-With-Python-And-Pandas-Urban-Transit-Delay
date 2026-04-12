# standardize_transit.py
# Milestone 5.36 - Standardizing Column Names
#                  and Data Formats
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate column name standardization,
#          naming conventions, text normalization,
#          and numeric format cleaning

import pandas as pd
import numpy as np
import re

print("=" * 57)
print("  MILESTONE 5.36 - STANDARDIZING COLUMN NAMES")
print("  AND DATA FORMATS")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Create a messy dataset
# Simulates raw data from a real transit authority
# with all the common formatting problems
# ─────────────────────────────────────────────────────

print("\n--- SETUP: Raw Messy Transit Dataset ---")
print("(simulating real-world inconsistent data)\n")

raw_data = {
    "Trip ID"           : ["T001","T002","T003",
                           "T004","T005","T006",
                           "T007","T008","T009","T010"],
    "Route Name"        : ["route_42","ROUTE_7",
                           "Route_15","route 23",
                           "ROUTE_42","route_7",
                           "Route 15","ROUTE_23",
                           "route_42","Route_7"],
    "DAY OF WEEK"       : ["Monday","monday",
                           "MONDAY","Tuesday",
                           "tuesday","WEDNESDAY",
                           "Wednesday","thursday",
                           "FRIDAY","Friday"],
    "Scheduled  Time"   : ["07:00","07:30","08:00",
                           "07:15","08:30","07:00",
                           "09:00","07:30","08:00",
                           "07:15"],
    "ActualTime"        : ["07:17","08:01","08:04",
                           "07:15","08:52","07:34",
                           "09:03","07:32","08:18",
                           "07:19"],
    "Delay (Minutes)"   : ["17","31","4","0","22",
                           "34","3","2","18","4"],
    "  Status  "        : ["  Minor Delay ",
                           "Severe Delay",
                           " On Time",
                           "On Time  ",
                           "  Major Delay  ",
                           "Severe Delay ",
                           " On Time ",
                           "On Time",
                           "Major Delay",
                           " Minor Delay"],
    "PassengerCount"    : ["42","None","38","55",
                           "61","None","29","44",
                           "57","33"],
    "Peak_Hour?"        : ["Yes","Yes","Yes","No",
                           "yes","YES","No","no",
                           "YES","Yes"],
}

df_raw = pd.DataFrame(raw_data)

print("Raw dataset column names:")
for i, col in enumerate(df_raw.columns):
    print(f"  [{i}] '{col}'")

print(f"\nRaw data preview (first 5 rows):")
print(df_raw.head(5).to_string())

# ─────────────────────────────────────────────────────
# SECTION 1 - STANDARDIZING COLUMN NAMES
# Goal: all lowercase, underscores not spaces,
#       no special characters, no leading/trailing
#       spaces, descriptive but concise
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Standardizing Column Names ---")
print()

# Step by step transformation
print("Step-by-step column name cleaning:\n")

original_cols = list(df_raw.columns)

# Step 1 — strip leading/trailing whitespace
step1 = [col.strip() for col in original_cols]

# Step 2 — convert to lowercase
step2 = [col.lower() for col in step1]

# Step 3 — replace spaces with underscore
step3 = [col.replace(" ", "_") for col in step2]

# Step 4 — remove special characters
#           keep only letters, numbers, underscores
step4 = [re.sub(r'[^a-z0-9_]', '', col)
         for col in step3]

# Step 5 — collapse multiple underscores
step5 = [re.sub(r'_+', '_', col).strip('_')
         for col in step4]

# Step 6 — apply meaningful rename mapping
rename_map = {
    "trip_id"          : "trip_id",
    "route_name"       : "route_id",
    "day_of_week"      : "day_of_week",
    "scheduled__time"  : "scheduled_time",
    "actualtime"       : "actual_time",
    "delay_minutes"    : "delay_minutes",
    "status"           : "status",
    "passengercount"   : "passenger_count",
    "peak_hour"        : "is_peak_hour",
}

print(f"  {'Original':<22} {'After Clean':<22} "
      f"{'Final Name'}")
print("  " + "-" * 60)

for orig, s1, s2, s3, s4, s5 in zip(
        original_cols, step1, step2,
        step3, step4, step5):
    final = rename_map.get(s5, s5)
    print(f"  {orig:<22} {s5:<22} {final}")

# Apply the full transformation
df_clean = df_raw.copy()
df_clean.columns = step5

# Apply rename for meaningful names
df_clean = df_clean.rename(columns=rename_map)

print(f"\nFinal standardized column names:")
for i, col in enumerate(df_clean.columns):
    print(f"  [{i}] {col}")

print()
print("Column naming rules applied:")
print("  snake_case      : all words separated by _")
print("  all lowercase   : no CAPS anywhere")
print("  no spaces       : replaced with underscore")
print("  no special chars: () [] ? removed")
print("  descriptive     : passengercount → "
      "passenger_count")

# ─────────────────────────────────────────────────────
# SECTION 2 - STANDARDIZING TEXT DATA
# Goal: consistent values in each text column
# route_id → lowercase with underscore
# day_of_week → Title Case (Monday not monday)
# status → Title Case, trimmed whitespace
# is_peak_hour → True/False boolean
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Standardizing Text Data ---")
print()

# 2a — route_id: normalize to consistent format
print("2a. route_id — before standardization:")
print(f"  {df_clean['route_id'].tolist()}")

df_clean['route_id'] = (
    df_clean['route_id']
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r'[^a-z0-9_]', '', regex=True)
)

# Normalize to Route_XX format
def normalize_route(route_str):
    """Convert any route format to Route_XX."""
    match = re.search(r'(\d+)', str(route_str))
    if match:
        return f"Route_{match.group(1)}"
    return route_str

df_clean['route_id'] = \
    df_clean['route_id'].apply(normalize_route)

print("route_id — after standardization:")
print(f"  {df_clean['route_id'].tolist()}")

# 2b — day_of_week: Title Case + strip
print("\n2b. day_of_week — before:")
print(f"  {df_clean['day_of_week'].tolist()}")

df_clean['day_of_week'] = (
    df_clean['day_of_week']
    .str.strip()
    .str.title()
)

print("day_of_week — after Title Case:")
print(f"  {df_clean['day_of_week'].tolist()}")

# 2c — status: strip whitespace + Title Case
print("\n2c. status — before (with whitespace):")
print(f"  {df_clean['status'].tolist()}")

df_clean['status'] = (
    df_clean['status']
    .str.strip()
    .str.title()
)

print("status — after strip + Title Case:")
print(f"  {df_clean['status'].tolist()}")

# 2d — is_peak_hour: convert Yes/No to True/False
print("\n2d. is_peak_hour — before:")
print(f"  {df_clean['is_peak_hour'].tolist()}")

df_clean['is_peak_hour'] = (
    df_clean['is_peak_hour']
    .str.strip()
    .str.lower()
    .map({'yes': True, 'no': False})
)

print("is_peak_hour — after bool conversion:")
print(f"  {df_clean['is_peak_hour'].tolist()}")
print(f"  dtype: {df_clean['is_peak_hour'].dtype}")

# ─────────────────────────────────────────────────────
# SECTION 3 - STANDARDIZING NUMERIC DATA
# delay_minutes and passenger_count loaded as strings
# Convert to correct numeric types
# Handle 'None' strings as NaN
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Standardizing Numeric Data ---")
print()

# 3a — delay_minutes: string → integer
print("3a. delay_minutes dtype before:")
print(f"  {df_clean['delay_minutes'].dtype} "
      f"— values: "
      f"{df_clean['delay_minutes'].tolist()}")

df_clean['delay_minutes'] = pd.to_numeric(
    df_clean['delay_minutes'],
    errors='coerce'
).astype('Int64')

print("delay_minutes dtype after:")
print(f"  {df_clean['delay_minutes'].dtype} "
      f"— values: "
      f"{df_clean['delay_minutes'].tolist()}")

# 3b — passenger_count: string 'None' → NaN → integer
print("\n3b. passenger_count before:")
print(f"  {df_clean['passenger_count'].tolist()}")
print(f"  dtype: {df_clean['passenger_count'].dtype}")

# Replace string 'None' with actual NaN first
df_clean['passenger_count'] = \
    df_clean['passenger_count'].replace('None', np.nan)

# Convert to numeric
df_clean['passenger_count'] = pd.to_numeric(
    df_clean['passenger_count'],
    errors='coerce'
).astype('Int64')

print("passenger_count after:")
print(f"  {df_clean['passenger_count'].tolist()}")
print(f"  dtype: {df_clean['passenger_count'].dtype}")

# ─────────────────────────────────────────────────────
# SECTION 4 - STANDARDIZING TIME FORMATS
# scheduled_time and actual_time as strings HH:MM
# Confirm consistent format
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Standardizing Time Formats ---")
print()

# Verify time format consistency
print("4a. scheduled_time values:")
print(f"  {df_clean['scheduled_time'].tolist()}")

print("\n4b. actual_time values:")
print(f"  {df_clean['actual_time'].tolist()}")

# Validate HH:MM format
def is_valid_time(t):
    """Check if string matches HH:MM format."""
    if pd.isna(t):
        return False
    return bool(re.match(r'^\d{2}:\d{2}$', str(t)))

sched_valid = df_clean['scheduled_time']\
    .apply(is_valid_time).all()
actual_valid = df_clean['actual_time']\
    .apply(is_valid_time).all()

print(f"\nTime format validation:")
print(f"  scheduled_time all HH:MM : {sched_valid}")
print(f"  actual_time all HH:MM    : {actual_valid}")

# ─────────────────────────────────────────────────────
# SECTION 5 - BEFORE AND AFTER COMPARISON
# Full summary of all changes made
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Before vs After Comparison ---")
print()

print("Column names comparison:")
print(f"  {'Before':<25} {'After'}")
print("  " + "-" * 45)
for orig, new in zip(df_raw.columns,
                     df_clean.columns):
    changed = "←" if orig.strip() != new else " "
    print(f"  {orig:<25} {new} {changed}")

print(f"\nData types comparison:")
print(f"  {'Column':<20} {'Before':<12} After")
print("  " + "-" * 40)
for col_raw, col_clean in zip(df_raw.columns,
                               df_clean.columns):
    before_dtype = str(df_raw[col_raw].dtype)
    after_dtype  = str(df_clean[col_clean].dtype)
    changed = "← CHANGED" \
        if before_dtype != after_dtype else ""
    print(f"  {col_clean:<20} {before_dtype:<12} "
          f"{after_dtype} {changed}")

print(f"\nFinal cleaned dataset:")
print(df_clean.to_string())

# Save to processed
import os
os.makedirs("data/processed", exist_ok=True)
df_clean.to_csv(
    "data/processed/transit_trips_standardized.csv",
    index=False
)
print(f"\nSaved to: "
      f"data/processed/transit_trips_standardized.csv")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.36 - Standardization Complete")
print("=" * 57)