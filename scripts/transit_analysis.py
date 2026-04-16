# transit_analysis.py
# Milestone 5.13 - First Python Script for Data Analysis
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate script-based data analysis workflow

# ─────────────────────────────────────────
# SECTION 1 - Sample Transit Data
# ─────────────────────────────────────────

# Simulated bus trip records
# Each entry: [route_id, scheduled_arrival, actual_arrival, day_type]
trip_data = [
    ["Route_42", "08:00", "08:14", "weekday"],
    ["Route_42", "08:30", "08:47", "weekday"],
    ["Route_15", "07:45", "07:48", "weekday"],
    ["Route_15", "08:15", "08:19", "weekday"],
    ["Route_7",  "09:00", "09:22", "weekday"],
    ["Route_7",  "09:30", "09:51", "weekday"],
    ["Route_23", "08:00", "08:03", "weekday"],
    ["Route_23", "08:45", "08:46", "weekday"],
    ["Route_42", "17:00", "17:18", "weekday"],
    ["Route_15", "17:30", "17:35", "weekday"],
]

# Delay in minutes for each trip (actual - scheduled)
delay_minutes = [14, 17, 3, 4, 22, 21, 3, 1, 18, 5]

print("=" * 50)
print("  URBAN TRANSIT DELAY ANALYSIS")
print("  Milestone 5.13 - First Python Script")
print("=" * 50)

# ─────────────────────────────────────────
# SECTION 2 - Basic Delay Calculations
# ─────────────────────────────────────────

print("\n--- SECTION 1: Raw Trip Data ---")
print(f"Total trips recorded : {len(trip_data)}")
print(f"Total delay minutes  : {sum(delay_minutes)}")

average_delay = sum(delay_minutes) / len(delay_minutes)
max_delay = max(delay_minutes)
min_delay = min(delay_minutes)

print(f"Average delay        : {average_delay:.1f} minutes")
print(f"Maximum delay        : {max_delay} minutes")
print(f"Minimum delay        : {min_delay} minutes")

# ─────────────────────────────────────────
# SECTION 3 - Delay Per Route
# ─────────────────────────────────────────

print("\n--- SECTION 2: Delay Summary by Route ---")

# Group delays by route manually
route_delays = {}
for i in range(len(trip_data)):
    route = trip_data[i][0]
    delay = delay_minutes[i]
    if route not in route_delays:
        route_delays[route] = []
    route_delays[route].append(delay)

# Calculate and print average delay per route
for route, delays in route_delays.items():
    avg = sum(delays) / len(delays)
    total = sum(delays)
    print(f"{route}: avg delay = {avg:.1f} min | "
          f"total delay = {total} min | trips = {len(delays)}")

# ─────────────────────────────────────────
# SECTION 4 - Delay Classification
# ─────────────────────────────────────────

print("\n--- SECTION 3: Delay Classification ---")
print("Classification rules:")
print("  On Time      = delay < 5 minutes")
print("  Minor Delay  = delay 5 to 15 minutes")
print("  Severe Delay = delay > 15 minutes")
print()

on_time = 0
minor = 0
severe = 0

for delay in delay_minutes:
    if delay < 5:
        on_time += 1
    elif delay <= 15:
        minor += 1
    else:
        severe += 1

total = len(delay_minutes)
print(f"On Time      : {on_time} trips "
      f"({(on_time/total)*100:.1f}%)")
print(f"Minor Delay  : {minor} trips "
      f"({(minor/total)*100:.1f}%)")
print(f"Severe Delay : {severe} trips "
      f"({(severe/total)*100:.1f}%)")

# ─────────────────────────────────────────
# SECTION 5 - Most Problematic Route
# ─────────────────────────────────────────

print("\n--- SECTION 4: Most Problematic Route ---")

worst_route = None
worst_avg = 0

for route, delays in route_delays.items():
    avg = sum(delays) / len(delays)
    if avg > worst_avg:
        worst_avg = avg
        worst_route = route

print(f"Route with highest average delay: {worst_route}")
print(f"Average delay on {worst_route}: {worst_avg:.1f} minutes")
print(f"Recommendation: Investigate {worst_route} for")
print(f"scheduling or infrastructure issues.")

# ─────────────────────────────────────────
# SECTION 6 - Script vs Notebook Note
# ─────────────────────────────────────────

print("\n--- SECTION 5: Script vs Notebook ---")
print("This script runs top to bottom automatically.")
print("Unlike a notebook, there is no persistent state")
print("between runs. Every execution starts fresh.")
print("Scripts are ideal for repeatable, automated")
print("data workflows in production environments.")

print("\n" + "=" * 50)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Urban Transit Delay Analysis - 5.13")
print("=" * 50)