# loops_transit.py
# Milestone 5.17 - Using for and while Loops
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate for loops, while loops, break,
#          continue using transit domain examples

print("=" * 57)
print("  MILESTONE 5.17 - FOR AND WHILE LOOPS")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - FOR LOOP OVER A RANGE
# for loops repeat a fixed number of times
# range(start, stop, step) generates a sequence
# Transit use: simulate trip slots across peak hours
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: for Loop over range() ---")
print("Simulating morning peak hour trip slots\n")

print("Trip slots from 7am to 10am (every 30 mins):")
slot = 1
for hour in range(7, 10):
    for minute in [0, 30]:
        print(f"  Slot {slot:>2}: "
              f"{hour:02d}:{minute:02d}")
        slot += 1

print(f"\nTotal trip slots generated: {slot - 1}")

# ─────────────────────────────────────────────────────
# SECTION 2 - FOR LOOP OVER A LIST
# Iterating directly over list elements
# Transit use: process each route's delay record
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: for Loop over a List ---")
print("Processing delay records for each route\n")

route_delays = {
    "Route_7" : [22, 31, 18, 25, 34],
    "Route_15": [4,  3,  6,  2,  5],
    "Route_42": [14, 17, 20, 12, 19],
    "Route_23": [1,  2,  3,  1,  2],
}

print(f"{'Route':<12} {'Delays':<30} "
      f"{'Average':>8}")
print("-" * 55)

for route, delays in route_delays.items():
    avg = sum(delays) / len(delays)
    delays_str = str(delays)
    print(f"{route:<12} {delays_str:<30} "
          f"{avg:>7.1f} min")

# ─────────────────────────────────────────────────────
# SECTION 3 - FOR LOOP WITH ENUMERATE
# enumerate gives both index and value
# Transit use: number each trip record
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: for Loop with enumerate() ---")
print("Numbering trip records for logging\n")

trips = [
    ("Route_42", 17),
    ("Route_7",  31),
    ("Route_15",  4),
    ("Route_23",  2),
    ("Route_42", 22),
]

for index, (route, delay) in enumerate(trips, start=1):
    print(f"  Trip #{index:>2} | {route:<10} | "
          f"delay = {delay:>2} min")

# ─────────────────────────────────────────────────────
# SECTION 4 - WHILE LOOP
# while repeats as long as a condition is True
# Must update the condition variable to avoid
# infinite loop
# Transit use: keep checking delays until threshold
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: while Loop ---")
print("Scanning trips until severe delay found\n")

delay_queue = [3, 8, 12, 6, 34, 19, 5, 28]
index = 0
trips_checked = 0

print("Scanning delay queue:")
while index < len(delay_queue):
    delay = delay_queue[index]
    trips_checked += 1
    print(f"  Checking trip {index + 1}: "
          f"delay = {delay} min")

    if delay > 30:
        print(f"  → Severe delay found at trip "
              f"{index + 1}! Stopping scan.")
        break

    index += 1
else:
    print("  → All trips scanned. "
          "No severe delay found.")

print(f"\nTrips checked before stopping: {trips_checked}")

# ─────────────────────────────────────────────────────
# SECTION 5 - WHILE LOOP WITH COUNTER
# Classic counter-controlled while loop
# Transit use: track how many routes exceed threshold
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: while Loop with Counter ---")
print("Counting routes with avg delay above 10 min\n")

route_averages = {
    "Route_7" : 26.0,
    "Route_15":  4.0,
    "Route_42": 16.4,
    "Route_23":  1.8,
    "Route_56": 11.2,
    "Route_88":  7.3,
}

route_list = list(route_averages.items())
i = 0
problem_routes = []

while i < len(route_list):
    route, avg = route_list[i]
    if avg > 10:
        problem_routes.append(route)
        print(f"  {route}: avg = {avg} min → "
              f"FLAGGED")
    else:
        print(f"  {route}: avg = {avg} min → OK")
    i += 1

print(f"\nProblem routes found: {len(problem_routes)}")
print(f"Routes flagged: {problem_routes}")

# ─────────────────────────────────────────────────────
# SECTION 6 - BREAK AND CONTINUE
# break  → exit the loop immediately
# continue → skip current iteration, go to next
# Transit use: skip missing data, stop at threshold
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: break and continue ---")

# continue — skip None values in delay records
print("Using CONTINUE — skipping incomplete records:\n")

delay_records = [12, None, 8, None, 25, 6, None, 19]

valid_delays = []
skipped = 0

for delay in delay_records:
    if delay is None:
        skipped += 1
        print(f"  Skipping incomplete record "
              f"(None value)")
        continue
    valid_delays.append(delay)
    print(f"  Processing delay: {delay} min")

print(f"\n  Valid records  : {len(valid_delays)}")
print(f"  Skipped records: {skipped}")
print(f"  Valid delays   : {valid_delays}")

# break — stop processing after finding first
# critical route
print("\nUsing BREAK — stop at first critical route:\n")

all_routes = [
    {"route": "Route_23", "avg": 1.8},
    {"route": "Route_15", "avg": 4.0},
    {"route": "Route_42", "avg": 16.4},
    {"route": "Route_7",  "avg": 26.0},
    {"route": "Route_56", "avg": 11.2},
]

# Sort by avg descending to find worst first
all_routes.sort(key=lambda x: x["avg"], reverse=True)

print("  Scanning from worst to best route:")
for r in all_routes:
    print(f"  {r['route']}: avg = {r['avg']} min",
          end="")
    if r["avg"] > 20:
        print(" → CRITICAL — escalating immediately")
        break
    else:
        print(" → acceptable")

# ─────────────────────────────────────────────────────
# SECTION 7 - INFINITE LOOP PREVENTION
# Show the pattern that causes infinite loops
# and the correct fix
# ─────────────────────────────────────────────────────

print("\n--- SECTION 7: Avoiding Infinite Loops ---")
print()
print("WRONG pattern (do NOT run this):")
print("  count = 0")
print("  while count < 5:")
print("      print(count)")
print("      # count never increments → infinite loop")
print()
print("CORRECT pattern:")

count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1          # this line prevents infinite loop

print(f"\n  Loop ended safely at count = {count}")
print("  Rule: always update the variable that the")
print("  while condition depends on.")

# ─────────────────────────────────────────────────────
# SECTION 8 - FOR VS WHILE COMPARISON
# ─────────────────────────────────────────────────────

print("\n--- SECTION 8: for vs while Summary ---")
print()
print(f"  {'Loop Type':<12} {'Use When':<35} "
      f"{'Risk'}")
print(f"  {'-'*12} {'-'*35} {'-'*20}")
print(f"  {'for':<12} "
      f"{'Number of iterations known':<35} "
      f"{'Low — fixed sequence'}")
print(f"  {'while':<12} "
      f"{'Stop condition is data-dependent':<35} "
      f"{'Infinite loop if not careful'}")
print()
print("  In this project:")
print("  for   → loop over all trip records in a list")
print("  while → keep reading data until buffer empty")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.17 - Loops Verified")
print("=" * 57)