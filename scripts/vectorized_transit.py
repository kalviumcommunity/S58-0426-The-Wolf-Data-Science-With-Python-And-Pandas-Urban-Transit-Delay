# vectorized_transit.py
# Milestone 5.25 - Applying Vectorized Operations
#                  Instead of Python Loops
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate loop-based vs vectorized
#          NumPy operations using transit data

import numpy as np
import time

print("=" * 57)
print("  MILESTONE 5.25 - VECTORIZED OPERATIONS")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - LOOP vs VECTORIZED SIDE BY SIDE
# Same operation written two ways
# Loop   : iterate over each element manually
# Vector : operate on entire array at once
# Transit: convert delay seconds to minutes
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Loop vs Vectorized ---")
print()

# Raw delay data in seconds
delay_seconds = np.array([
    840, 1020, 180, 1860, 480,
    1140, 120, 1620, 660, 960
])

print(f"Raw delays (seconds) : {delay_seconds}")

# LOOP approach — slow, verbose
delay_minutes_loop = []
for sec in delay_seconds:
    delay_minutes_loop.append(sec / 60)

print(f"\nLoop result (minutes): "
      f"{[round(x, 1) for x in delay_minutes_loop]}")
print("  Loop used 3 lines + manual iteration")

# VECTORIZED approach — fast, clean
delay_minutes_vec = delay_seconds / 60

print(f"Vector result (mins) : "
      f"{np.round(delay_minutes_vec, 1)}")
print("  Vector used 1 line — same result")

# Verify both give identical results
are_equal = np.allclose(
    delay_minutes_loop,
    delay_minutes_vec
)
print(f"\nResults identical    : {are_equal}")
print("Vectorization is correct AND more readable")

# ─────────────────────────────────────────────────────
# SECTION 2 - VECTORIZED ARITHMETIC OPERATIONS
# All standard operators work element-wise on arrays
# Transit: calculate delay statistics across all trips
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Vectorized Arithmetic ---")
print()

# Sample delay data in minutes
delays = np.array([
    14, 22, 5, 31, 8,
    19, 3, 27, 11, 16,
    7,  25, 2, 18, 33
])

print(f"Delay array          : {delays}")
print(f"Shape                : {delays.shape}")
print(f"Data type            : {delays.dtype}")

# Arithmetic — all applied to every element at once
print("\nVectorized arithmetic operations:")
print(f"  delays + 5         : {delays + 5}")
print(f"  delays * 2         : {delays * 2}")
print(f"  delays - 2         : {delays - 2}")
print(f"  delays / 60        : "
      f"{np.round(delays / 60, 3)}")
print(f"  delays ** 2        : {delays ** 2}")

# Aggregate functions — operate on whole array
print("\nAggregate operations:")
print(f"  np.sum(delays)     : {np.sum(delays)}")
print(f"  np.mean(delays)    : "
      f"{np.mean(delays):.2f} min")
print(f"  np.max(delays)     : {np.max(delays)} min")
print(f"  np.min(delays)     : {np.min(delays)} min")
print(f"  np.std(delays)     : "
      f"{np.std(delays):.2f} min")
print(f"  np.median(delays)  : "
      f"{np.median(delays):.1f} min")

# Two arrays — element-wise operations
scheduled = np.array([
    480, 510, 540, 570, 600,
    630, 660, 690, 720, 750
])
actual = np.array([
    494, 532, 545, 601, 608,
    649, 663, 717, 731, 766
])

computed_delays = actual - scheduled
print(f"\nElement-wise subtraction (actual - scheduled):")
print(f"  Scheduled          : {scheduled}")
print(f"  Actual             : {actual}")
print(f"  Computed delays    : {computed_delays} min")

# ─────────────────────────────────────────────────────
# SECTION 3 - VECTORIZED COMPARISONS
# Comparison operators return boolean arrays
# Each element is True or False based on condition
# Transit: find which trips exceed delay threshold
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Vectorized Comparisons ---")
print()

print(f"Delay array          : {delays}")

# Boolean array from comparison
is_delayed      = delays >= 5
is_severe       = delays > 20
is_on_time      = delays < 5

print(f"\nBoolean comparisons:")
print(f"  delays >= 5        : {is_delayed}")
print(f"  delays > 20        : {is_severe}")
print(f"  delays < 5         : {is_on_time}")

# Count using boolean sum (True = 1, False = 0)
print(f"\nCounting with boolean arrays:")
print(f"  Delayed trips      : "
      f"{np.sum(is_delayed)} of {len(delays)}")
print(f"  Severe trips       : "
      f"{np.sum(is_severe)} of {len(delays)}")
print(f"  On-time trips      : "
      f"{np.sum(is_on_time)} of {len(delays)}")

# Percentage calculation — vectorized
delay_pct  = np.sum(is_delayed) / len(delays) * 100
severe_pct = np.sum(is_severe)  / len(delays) * 100
print(f"\nPercentages:")
print(f"  Delay rate         : {delay_pct:.1f}%")
print(f"  Severe delay rate  : {severe_pct:.1f}%")

# Boolean indexing — filter array with mask
severe_delays = delays[is_severe]
print(f"\nBoolean indexing — severe delays only:")
print(f"  delays[delays > 20]: {severe_delays}")

# ─────────────────────────────────────────────────────
# SECTION 4 - VECTORIZED CONDITIONS WITH np.where
# np.where(condition, value_if_true, value_if_false)
# Replaces if-else loops completely
# Transit: classify each delay without a loop
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: np.where() ---")
print()
print("np.where replaces element-wise if-else loops")
print()

# Simple classification
status_simple = np.where(
    delays >= 5,
    "Delayed",
    "On Time"
)
print(f"delays             : {delays}")
print(f"np.where(>=5)      : {status_simple}")

# Nested np.where for multiple categories
# equivalent to if-elif-else on every element
status_full = np.where(
    delays < 5,  "On Time",
    np.where(
        delays <= 15, "Minor",
        np.where(
            delays <= 30, "Major",
            "Severe"
        )
    )
)

print(f"\nFull classification (no loop needed):")
for i in range(len(delays)):
    print(f"  delay={delays[i]:>2} min → "
          f"{status_full[i]}")

# ─────────────────────────────────────────────────────
# SECTION 5 - PERFORMANCE COMPARISON
# Show timing difference between loop and vector
# on a large array
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Performance Comparison ---")
print()

# Large array — 100,000 trip delay values
large_delays = np.random.randint(0, 60,
                                  size=100_000)
print(f"Array size           : "
      f"{len(large_delays):,} trip records")

# LOOP timing
start = time.time()
loop_result = []
for d in large_delays:
    loop_result.append(d * 2)
loop_time = time.time() - start

# VECTORIZED timing
start = time.time()
vec_result = large_delays * 2
vec_time = time.time() - start

print(f"\nOperation: multiply every delay by 2")
print(f"  Loop time          : "
      f"{loop_time:.6f} seconds")
print(f"  Vector time        : "
      f"{vec_time:.6f} seconds")

if loop_time > 0 and vec_time > 0:
    speedup = loop_time / vec_time
    print(f"  Speedup            : "
          f"{speedup:.1f}x faster")

# Verify results match
match = np.allclose(loop_result, vec_result)
print(f"  Results match      : {match}")
print(f"\nVectorized is faster AND produces same result")

# ─────────────────────────────────────────────────────
# SECTION 6 - FULL TRANSIT ANALYSIS VECTORIZED
# Complete pipeline using only vectorized operations
# No loops anywhere in the analysis
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Full Vectorized Pipeline ---")
print()

# Simulated dataset
np.random.seed(42)
n_trips = 500

route_ids    = np.random.choice(
    [7, 15, 42, 23], size=n_trips
)
delay_data   = np.random.randint(0, 45, size=n_trips)
hour_data    = np.random.randint(6, 22, size=n_trips)

print(f"Dataset size         : {n_trips} trips")
print()

# All operations vectorized — no loops
total_trips   = len(delay_data)
avg_delay     = np.mean(delay_data)
severe_mask   = delay_data > 30
peak_mask     = (hour_data >= 7) & (hour_data <= 9) | \
                (hour_data >= 17) & (hour_data <= 19)
peak_severe   = severe_mask & peak_mask

print("Fleet-wide statistics (all vectorized):")
print(f"  Total trips        : {total_trips:,}")
print(f"  Average delay      : {avg_delay:.1f} min")
print(f"  Severe delays      : "
      f"{np.sum(severe_mask):,} trips "
      f"({np.sum(severe_mask)/total_trips*100:.1f}%)")
print(f"  Peak hour trips    : "
      f"{np.sum(peak_mask):,} trips")
print(f"  Peak+severe alerts : "
      f"{np.sum(peak_severe):,} trips")

# Per-route stats — vectorized per route
print("\nPer-route analysis (vectorized):")
print(f"  {'Route':<10} {'Trips':>6} "
      f"{'Avg Delay':>10} {'Severe':>8}")
print("  " + "-" * 38)

for route_id in [7, 15, 42, 23]:
    mask       = route_ids == route_id
    route_dels = delay_data[mask]
    avg        = np.mean(route_dels)
    sev        = np.sum(route_dels > 30)
    print(f"  Route_{route_id:<4} "
          f"{np.sum(mask):>6} "
          f"{avg:>9.1f}m "
          f"{sev:>8} trips")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.25 - Vectorization Verified")
print("=" * 57)