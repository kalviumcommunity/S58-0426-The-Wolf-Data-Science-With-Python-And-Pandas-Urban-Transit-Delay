# compare_distributions_transit.py
# Milestone 5.38 - Comparing Distributions Across
#                  Multiple Columns
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate multi-column distribution
#          comparison using central tendency,
#          spread, skew, and cross-group analysis

import pandas as pd
import numpy as np

print("=" * 57)
print("  MILESTONE 5.38 - COMPARING DISTRIBUTIONS")
print("  Across Multiple Columns")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SETUP - Create full transit dataset
# ─────────────────────────────────────────────────────

print("\n--- SETUP: Transit Dataset ---\n")

np.random.seed(42)

data = {
    "trip_id": [f"T{str(i).zfill(3)}"
                for i in range(1, 41)],
    "route_id": (
        ["Route_42"] * 10 +
        ["Route_7"]  * 10 +
        ["Route_15"] * 10 +
        ["Route_23"] * 10
    ),
    "day_of_week": [
        "Monday","Monday","Tuesday","Tuesday",
        "Wednesday","Wednesday","Thursday","Thursday",
        "Friday","Friday"
    ] * 4,
    "hour_of_day": (
        [8, 9, 7, 8, 17, 18, 8, 7, 9, 17] * 4
    ),
    "delay_minutes": (
        # Route_42 — moderate delays
        [14, 17, 20, 12, 19, 22, 8, 15, 25, 18] +
        # Route_7 — severe delays
        [31, 28, 34, 22, 38, 41, 19, 35, 29, 33] +
        # Route_15 — mostly on time
        [4,  3,  6,  2,  7,  5,  1,  8,  3,  4] +
        # Route_23 — very reliable
        [1,  2,  0,  3,  2,  1,  4,  0,  2,  1]
    ),
    "passenger_count": (
        [42, 58, 38, 55, 61, 67, 29, 44, 57, 63] +
        [51, 62, 45, 58, 70, 48, 55, 66, 43, 59] +
        [35, 41, 29, 47, 38, 44, 32, 50, 36, 42] +
        [28, 35, 22, 40, 31, 38, 25, 44, 30, 36]
    ),
    "scheduled_duration": (
        [45] * 10 + [60] * 10 +
        [30] * 10 + [25] * 10
    ),
    "actual_duration": (
        # Route_42 — moderate overrun
        [59, 62, 65, 57, 64, 67, 53, 60, 70, 63] +
        # Route_7 — severe overrun
        [91, 88, 94, 82, 98,101, 79, 95, 89, 93] +
        # Route_15 — slight overrun
        [34, 33, 36, 32, 37, 35, 31, 38, 33, 34] +
        # Route_23 — nearly on schedule
        [26, 27, 25, 28, 27, 26, 29, 25, 27, 26]
    ),
    "status": (
        ["Minor Delay","Minor Delay","Major Delay",
         "Minor Delay","Major Delay","Major Delay",
         "Minor Delay","Minor Delay","Major Delay",
         "Major Delay"] +
        ["Severe Delay"] * 8 +
        ["Major Delay","Severe Delay"] +
        ["On Time","On Time","Minor Delay","On Time",
         "Minor Delay","On Time","On Time","Minor Delay",
         "On Time","On Time"] +
        ["On Time"] * 10
    )
}

df = pd.DataFrame(data)
print(f"Dataset shape        : {df.shape}")
print(f"Routes               : "
      f"{df['route_id'].unique()}")
print(f"Numeric columns      : "
      f"{list(df.select_dtypes('number').columns)}")

# ─────────────────────────────────────────────────────
# SECTION 1 - WHAT A DISTRIBUTION MEANS
# Distribution = how values are spread across range
# Described by: center, spread, shape, extremes
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Understanding Distributions ---")
print()

print("A distribution describes how values")
print("are spread across their possible range.\n")
print("Four properties define a distribution:")
print()

properties = [
    ("Center",
     "Where values cluster (mean, median)",
     "Avg delay = 15 min"),
    ("Spread",
     "How wide values range (std, IQR, range)",
     "Delays between 2 and 41 min"),
    ("Shape",
     "Symmetric or skewed toward extremes",
     "More very-late trips than very-early"),
    ("Outliers",
     "Values far from the rest",
     "One 120-min breakdown delay"),
]

print(f"  {'Property':<10} {'Definition':<42} "
      f"Transit Example")
print("  " + "-" * 70)
for prop, defn, example in properties:
    print(f"  {prop:<10} {defn:<42} {example}")

print()
print("Comparing distributions asks:")
print("  'Is delay_minutes spread differently")
print("   than passenger_count?'")
print("  'Does Route_7 have a different delay")
print("   distribution than Route_23?'")

# ─────────────────────────────────────────────────────
# SECTION 2 - COMPARING CENTRAL TENDENCY
# Mean and median side by side for all numeric cols
# Mean-median gap reveals skewness
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Comparing Central Tendency ---")
print()

num_cols = ['delay_minutes', 'passenger_count',
            'scheduled_duration', 'actual_duration']

print("Mean vs Median comparison:\n")
print(f"  {'Column':<22} {'Mean':>8} "
      f"{'Median':>8} {'Gap':>8} Skew")
print("  " + "-" * 58)

for col in num_cols:
    mean   = df[col].mean()
    median = df[col].median()
    gap    = mean - median
    if gap > 2:
        skew = "RIGHT (mean > median)"
    elif gap < -2:
        skew = "LEFT  (mean < median)"
    else:
        skew = "SYMMETRIC"
    print(f"  {col:<22} {mean:>8.1f} "
          f"{median:>8.1f} {gap:>8.1f} {skew}")

print()
print("Interpretation:")
print("  delay_minutes: right-skewed → a few very")
print("  large delays pull mean above median")
print("  passenger_count: near-symmetric → balanced")
print("  distribution around a central value")
print("  actual_duration: right-skewed → overruns")
print("  are more extreme than underruns")

# ─────────────────────────────────────────────────────
# SECTION 3 - COMPARING SPREAD AND VARIABILITY
# Std, IQR, and range side by side
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Comparing Spread ---")
print()

print("Spread comparison — std, IQR, range:\n")
print(f"  {'Column':<22} {'Std':>7} "
      f"{'IQR':>7} {'Range':>7} {'CV%':>7}")
print("  " + "-" * 56)

for col in num_cols:
    std  = df[col].std()
    iqr  = (df[col].quantile(0.75) -
            df[col].quantile(0.25))
    rng  = df[col].max() - df[col].min()
    mean = df[col].mean()
    cv   = (std / mean) * 100  # coefficient of variation
    print(f"  {col:<22} {std:>7.1f} "
          f"{iqr:>7.1f} {rng:>7.1f} {cv:>6.1f}%")

print()
print("CV% = Coefficient of Variation")
print("    = (std / mean) × 100")
print("    = relative spread regardless of scale")
print()
print("Interpretation:")
print("  High CV% = high variability relative to mean")
print("  delay_minutes has high CV → very inconsistent")
print("  scheduled_duration has low CV → fixed routes")
print("  are consistent by design")

# ─────────────────────────────────────────────────────
# SECTION 4 - PERCENTILE COMPARISON
# Shows distribution shape across columns
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Percentile Comparison ---")
print()

percentiles = [0.10, 0.25, 0.50, 0.75, 0.90]
pct_labels  = ['P10', 'P25', 'P50', 'P75', 'P90']

print("Percentile profile — each column:\n")
print(f"  {'Percentile':<12}", end="")
for col in num_cols:
    short = col.replace('_', ' ')[:18]
    print(f" {short:>18}", end="")
print()
print("  " + "-" * 84)

for pct, label in zip(percentiles, pct_labels):
    print(f"  {label:<12}", end="")
    for col in num_cols:
        val = df[col].quantile(pct)
        print(f" {val:>18.1f}", end="")
    print()

print()
print("Reading this table:")
print("  P10 = 10% of trips had LESS than this value")
print("  P90 = 90% of trips had LESS than this value")
print("  Wide P10-P90 gap = more spread out data")
print()
delay_p10 = df['delay_minutes'].quantile(0.10)
delay_p90 = df['delay_minutes'].quantile(0.90)
pax_p10   = df['passenger_count'].quantile(0.10)
pax_p90   = df['passenger_count'].quantile(0.90)
print(f"  delay_minutes P10-P90 span   : "
      f"{delay_p10:.1f} to {delay_p90:.1f} min "
      f"(width = {delay_p90-delay_p10:.1f})")
print(f"  passenger_count P10-P90 span : "
      f"{pax_p10:.1f} to {pax_p90:.1f} pax "
      f"(width = {pax_p90-pax_p10:.1f})")

# ─────────────────────────────────────────────────────
# SECTION 5 - COMPARING DELAY DISTRIBUTIONS BY ROUTE
# GroupBy + describe to compare same column
# across different groups
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Delay Distribution by Route ---")
print()

route_dist = df.groupby('route_id')[
    'delay_minutes'
].agg(
    count='count',
    mean='mean',
    median='median',
    std='std',
    min='min',
    p25=lambda x: x.quantile(0.25),
    p75=lambda x: x.quantile(0.75),
    max='max'
).round(1)

print("delay_minutes distribution per route:")
print(route_dist.to_string())

print()
print("Distribution comparison findings:")
print()

for route in df['route_id'].unique():
    mean   = route_dist.loc[route, 'mean']
    std    = route_dist.loc[route, 'std']
    mn     = route_dist.loc[route, 'min']
    mx     = route_dist.loc[route, 'max']
    median = route_dist.loc[route, 'median']

    if mean > 25:
        label = "CRITICAL"
    elif mean > 10:
        label = "POOR"
    elif mean > 4:
        label = "MODERATE"
    else:
        label = "GOOD"

    print(f"  {route}: mean={mean:.1f} "
          f"std={std:.1f} "
          f"range={mn:.0f}-{mx:.0f} "
          f"→ {label}")

# ─────────────────────────────────────────────────────
# SECTION 6 - COMPARING WEEKDAY vs WEEKEND
# Same delay column, split by day type
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Weekday vs Weekend ---")
print()

weekend_days = ['Saturday', 'Sunday']
df['is_weekend'] = df['day_of_week'].isin(
    weekend_days
)

# Our dataset has no weekends — simulate comparison
# by splitting Monday/Friday as proxy
early_week = df[df['day_of_week'].isin(
    ['Monday', 'Tuesday']
)]['delay_minutes']

late_week  = df[df['day_of_week'].isin(
    ['Thursday', 'Friday']
)]['delay_minutes']

print("Early week (Mon-Tue) vs Late week (Thu-Fri):\n")
print(f"  {'Statistic':<12} "
      f"{'Mon-Tue':>10} {'Thu-Fri':>10} "
      f"{'Difference':>12}")
print("  " + "-" * 46)

stats_to_compare = [
    ('count',  early_week.count(),
     late_week.count()),
    ('mean',   early_week.mean(),
     late_week.mean()),
    ('median', early_week.median(),
     late_week.median()),
    ('std',    early_week.std(),
     late_week.std()),
    ('min',    early_week.min(),
     late_week.min()),
    ('max',    early_week.max(),
     late_week.max()),
]

for stat, val1, val2 in stats_to_compare:
    diff = val2 - val1
    direction = "↑" if diff > 0 else "↓" \
                if diff < 0 else "="
    print(f"  {stat:<12} {val1:>10.1f} "
          f"{val2:>10.1f} "
          f"{diff:>10.1f} {direction}")

# ─────────────────────────────────────────────────────
# SECTION 7 - CORRELATION BETWEEN COLUMNS
# How columns move together
# ─────────────────────────────────────────────────────

print("\n--- SECTION 7: Column Correlations ---")
print()

corr_cols = ['delay_minutes', 'passenger_count',
             'hour_of_day', 'actual_duration']
corr_matrix = df[corr_cols].corr().round(2)

print("Correlation matrix:")
print(corr_matrix.to_string())

print()
print("Interpreting correlations:")
print("  +1.0 = perfect positive relationship")
print("   0.0 = no relationship")
print("  -1.0 = perfect negative relationship")
print()

# Key correlations
delay_pax   = corr_matrix.loc[
    'delay_minutes', 'passenger_count'
]
delay_actual = corr_matrix.loc[
    'delay_minutes', 'actual_duration'
]

print(f"  delay vs passenger_count : "
      f"{delay_pax:.2f}")
if abs(delay_pax) > 0.3:
    direction = "more" if delay_pax > 0 else "fewer"
    print(f"    → {direction} passengers correlate "
          f"with {'higher' if delay_pax > 0 else 'lower'}"
          f" delays")
else:
    print(f"    → weak correlation — "
          f"passenger load may not drive delays")

print(f"\n  delay vs actual_duration : "
      f"{delay_actual:.2f}")
if abs(delay_actual) > 0.5:
    print(f"    → strong positive — delayed trips")
    print(f"       take longer to complete")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.38 - Distributions Compared")
print("=" * 57)