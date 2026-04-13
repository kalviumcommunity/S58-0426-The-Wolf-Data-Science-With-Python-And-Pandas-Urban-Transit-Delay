# summary_stats_transit.py
# Milestone 5.37 - Computing Basic Summary Statistics
#                  for Individual Columns
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate mean, median, std, min, max,
#          percentiles, and comparative statistics
#          using transit domain data

import pandas as pd
import numpy as np

print("=" * 57)
print("  MILESTONE 5.37 - SUMMARY STATISTICS")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Create full transit dataset
# ─────────────────────────────────────────────────────

print("\n--- SETUP: Transit Dataset ---\n")

data = {
    "trip_id": [
        "T001","T002","T003","T004","T005",
        "T006","T007","T008","T009","T010",
        "T011","T012","T013","T014","T015",
        "T016","T017","T018","T019","T020",
        "T021","T022","T023","T024","T025",
        "T026","T027","T028","T029","T030"
    ],
    "route_id": [
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7","Route_15","Route_23",
        "Route_42","Route_7"
    ],
    "day_of_week": [
        "Monday","Monday","Tuesday","Tuesday",
        "Wednesday","Wednesday","Thursday","Thursday",
        "Friday","Friday","Monday","Tuesday",
        "Wednesday","Thursday","Friday","Monday",
        "Tuesday","Wednesday","Thursday","Friday",
        "Monday","Monday","Tuesday","Tuesday",
        "Wednesday","Wednesday","Thursday","Thursday",
        "Friday","Friday"
    ],
    "hour_of_day": [
        8, 9, 7, 8, 17, 18, 8, 7, 9, 17,
        8, 18, 7, 9, 8, 17, 8, 7, 9, 17,
        8, 9, 7, 8, 17, 18, 8, 7, 9, 17
    ],
    "delay_minutes": [
        14, 31,  5,  0, 22, 34,  3,  2, 18, 18,
         7,  1, 21, 34,  8,  3, 37,  2,  4, 14,
        17, 28,  6,  0, 19, 41,  5,  1, 23, 35
    ],
    "passenger_count": [
        42, 58, 38, 55, 61, 67, 29, 44, 57, 63,
        33, 48, 52, 62, 41, 36, 39, 52, 47, 59,
        44, 61, 35, 50, 58, 70, 31, 43, 55, 66
    ],
    "scheduled_duration": [
        45, 60, 30, 25, 45, 60, 30, 25, 45, 60,
        30, 25, 45, 60, 30, 25, 45, 60, 30, 25,
        45, 60, 30, 25, 45, 60, 30, 25, 45, 60
    ],
    "status": [
        "Minor Delay","Severe Delay","On Time",
        "On Time","Major Delay","Severe Delay",
        "On Time","On Time","Major Delay",
        "Major Delay","Minor Delay","On Time",
        "Major Delay","Severe Delay","Minor Delay",
        "On Time","Severe Delay","On Time",
        "On Time","Minor Delay","Minor Delay",
        "Major Delay","On Time","On Time",
        "Major Delay","Severe Delay","On Time",
        "On Time","Major Delay","Severe Delay"
    ]
}

df = pd.DataFrame(data)
print(f"Dataset shape        : {df.shape}")
print(f"Numeric columns      : "
      f"{list(df.select_dtypes(include='number').columns)}")

# ─────────────────────────────────────────────────────
# SECTION 1 - WHAT EACH STATISTIC MEANS
# Conceptual explanation before computing
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: What Each Statistic Means ---")
print()
print("Applied to delay_minutes in transit context:\n")

stats_explained = [
    ("count",
     "How many trips have a delay value recorded",
     "Data completeness check"),
    ("mean",
     "Average delay across all trips",
     "Overall performance indicator"),
    ("median",
     "Middle value — half trips above, half below",
     "Typical experience for a commuter"),
    ("std",
     "How much delays vary from the average",
     "Reliability / consistency indicator"),
    ("min",
     "Shortest delay — best case trip",
     "Best possible experience"),
    ("max",
     "Longest delay — worst case trip",
     "Worst possible experience"),
    ("25th pct",
     "75% of trips had MORE delay than this",
     "Lower performance boundary"),
    ("75th pct",
     "25% of trips had MORE delay than this",
     "Upper performance boundary"),
]

print(f"  {'Statistic':<12} {'Meaning':<42} "
      f"Transit Interpretation")
print("  " + "-" * 75)
for stat, meaning, transit in stats_explained:
    print(f"  {stat:<12} {meaning:<42} {transit}")

# ─────────────────────────────────────────────────────
# SECTION 2 - STATISTICS FOR delay_minutes COLUMN
# Most important column for this project
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: delay_minutes Statistics ---")
print()

col = df['delay_minutes']

# Individual statistics
count  = col.count()
mean   = col.mean()
median = col.median()
std    = col.std()
var    = col.var()
mn     = col.min()
mx     = col.max()
p25    = col.quantile(0.25)
p75    = col.quantile(0.75)
iqr    = p75 - p25
rng    = mx - mn

print("Individual statistic methods:")
print(f"  col.count()         = {count}")
print(f"  col.mean()          = {mean:.2f} min")
print(f"  col.median()        = {median:.1f} min")
print(f"  col.std()           = {std:.2f} min")
print(f"  col.var()           = {var:.2f}")
print(f"  col.min()           = {mn} min")
print(f"  col.max()           = {mx} min")
print(f"  col.quantile(0.25)  = {p25:.1f} min")
print(f"  col.quantile(0.75)  = {p75:.1f} min")
print(f"  IQR (p75 - p25)     = {iqr:.1f} min")
print(f"  Range (max - min)   = {rng} min")

# describe() gives all at once
print(f"\ncol.describe() — all in one:")
print(col.describe().to_string())

# Interpretation
print(f"\nInterpretation of delay_minutes:")
print(f"  Mean   {mean:.1f} min vs "
      f"Median {median:.1f} min")
if mean > median:
    print(f"  Mean > Median → distribution is "
          f"RIGHT-SKEWED")
    print(f"  A few large delays pull the mean up")
    print(f"  Median is more representative of the")
    print(f"  TYPICAL commuter experience")
else:
    print(f"  Mean ≈ Median → roughly symmetric")

print(f"\n  IQR = {iqr:.1f} min — middle 50% of trips")
print(f"  fall within a {iqr:.1f} minute delay range")
print(f"  High IQR = inconsistent service quality")

# ─────────────────────────────────────────────────────
# SECTION 3 - STATISTICS FOR passenger_count COLUMN
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: passenger_count Statistics ---")
print()

pax = df['passenger_count']

print("passenger_count.describe():")
print(pax.describe().to_string())

print(f"\nKey metrics:")
print(f"  Average passengers per trip : "
      f"{pax.mean():.1f}")
print(f"  Median passengers per trip  : "
      f"{pax.median():.1f}")
print(f"  Least passengers (lightest) : {pax.min()}")
print(f"  Most passengers (busiest)   : {pax.max()}")
print(f"  Std deviation               : "
      f"{pax.std():.1f}")

print(f"\nInterpretation:")
print(f"  Average trip carries "
      f"{pax.mean():.0f} passengers")
print(f"  Busiest trip: {pax.max()} passengers")
print(f"  At avg delay {mean:.1f} min, each severe")
print(f"  delay affects ~{pax.mean():.0f} commuters")

# ─────────────────────────────────────────────────────
# SECTION 4 - MEAN vs MEDIAN — KEY DIFFERENCE
# Demonstrates how outliers affect mean but not median
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Mean vs Median Impact ---")
print()

# Normal delays
normal_delays = pd.Series([5, 8, 3, 12, 7,
                             6, 9, 4, 11, 8])
print(f"Normal delays        : "
      f"{list(normal_delays)}")
print(f"  Mean   : {normal_delays.mean():.1f} min")
print(f"  Median : {normal_delays.median():.1f} min")
print(f"  Difference: "
      f"{abs(normal_delays.mean()-normal_delays.median()):.1f} min")

# Same delays with one severe outlier (e.g. breakdown)
outlier_delays = pd.Series([5, 8, 3, 12, 7,
                              6, 9, 4, 11, 120])
print(f"\nWith breakdown (120 min added):")
print(f"  {list(outlier_delays)}")
print(f"  Mean   : {outlier_delays.mean():.1f} min "
      f"← jumped significantly")
print(f"  Median : {outlier_delays.median():.1f} min"
      f" ← barely changed")
print(f"  Difference: "
      f"{abs(outlier_delays.mean()-outlier_delays.median()):.1f} min")

print(f"\nConclusion:")
print(f"  Mean is sensitive to outliers")
print(f"  Median is resistant to outliers")
print(f"  For skewed transit delay data:")
print(f"  → Use MEDIAN for typical commuter")
print(f"    experience")
print(f"  → Use MEAN for total delay burden")
print(f"    calculation")

# ─────────────────────────────────────────────────────
# SECTION 5 - COMPARING STATISTICS ACROSS COLUMNS
# Side by side comparison of all numeric columns
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Comparing Columns ---")
print()

numeric_cols = ['delay_minutes',
                'passenger_count',
                'hour_of_day',
                'scheduled_duration']

print("Statistics across all numeric columns:\n")
print(f"  {'Statistic':<10}", end="")
for col_name in numeric_cols:
    print(f" {col_name:>20}", end="")
print()
print("  " + "-" * 90)

stats_list = [
    ("count",   lambda c: f"{c.count():.0f}"),
    ("mean",    lambda c: f"{c.mean():.2f}"),
    ("median",  lambda c: f"{c.median():.2f}"),
    ("std",     lambda c: f"{c.std():.2f}"),
    ("min",     lambda c: f"{c.min():.0f}"),
    ("max",     lambda c: f"{c.max():.0f}"),
    ("25%",     lambda c: f"{c.quantile(0.25):.2f}"),
    ("75%",     lambda c: f"{c.quantile(0.75):.2f}"),
]

for stat_name, func in stats_list:
    print(f"  {stat_name:<10}", end="")
    for col_name in numeric_cols:
        val = func(df[col_name])
        print(f" {val:>20}", end="")
    print()

# ─────────────────────────────────────────────────────
# SECTION 6 - PER-ROUTE STATISTICS
# GroupBy to compare statistics across routes
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Per-Route Statistics ---")
print()

route_stats = df.groupby('route_id')[
    'delay_minutes'
].agg(
    count='count',
    mean='mean',
    median='median',
    std='std',
    min='min',
    max='max'
).round(1)

print("delay_minutes statistics per route:")
print(route_stats.to_string())

print(f"\nKey findings:")
worst_mean  = route_stats['mean'].idxmax()
best_mean   = route_stats['mean'].idxmin()
most_varied = route_stats['std'].idxmax()

print(f"  Worst avg delay    : {worst_mean} "
      f"({route_stats.loc[worst_mean,'mean']} min)")
print(f"  Best avg delay     : {best_mean} "
      f"({route_stats.loc[best_mean,'mean']} min)")
print(f"  Most inconsistent  : {most_varied} "
      f"(std = "
      f"{route_stats.loc[most_varied,'std']} min)")
print(f"\n  High std means delays vary widely —")
print(f"  unpredictable service is as bad as")
print(f"  consistently late service")

# ─────────────────────────────────────────────────────
# SECTION 7 - VALUE COUNTS FOR CATEGORICAL COLUMN
# Summary statistics for non-numeric columns
# ─────────────────────────────────────────────────────

print("\n--- SECTION 7: Categorical Summary ---")
print()

print("Status column — value_counts():")
status_counts = df['status'].value_counts()
status_pct    = df['status'].value_counts(
    normalize=True
) * 100

print(f"\n  {'Status':<15} {'Count':>6} "
      f"{'Percentage':>12}")
print("  " + "-" * 36)
for status in status_counts.index:
    count = status_counts[status]
    pct   = status_pct[status]
    bar   = "█" * int(pct // 5)
    print(f"  {status:<15} {count:>6} "
          f"{pct:>10.1f}%  {bar}")

print(f"\n  mode()[0] = '{df['status'].mode()[0]}' "
      f"← most common status")
print(f"  nunique() = {df['status'].nunique()} "
      f"← unique categories")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.37 - Summary Stats Verified")
print("=" * 57)