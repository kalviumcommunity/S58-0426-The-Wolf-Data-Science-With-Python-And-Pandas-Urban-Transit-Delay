# conditionals_transit.py
# Milestone 5.16 - Writing Conditional Statements for Data Logic
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate if, elif, else and logical operators
#          using transit domain examples

print("=" * 57)
print("  MILESTONE 5.16 - CONDITIONAL STATEMENTS")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - BASIC IF STATEMENT
# if checks one condition — executes only when True
# Transit use: check if a trip is delayed at all
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Basic if Statement ---")
print("Checking if a trip has any delay\n")

delay_minutes = 14

print(f"Trip delay           : {delay_minutes} minutes")

if delay_minutes > 0:
    print("  Result: This trip is delayed.")
    print("  Action: Flag for reporting.")

# Test with zero delay
delay_minutes_2 = 0
print(f"\nTrip delay           : {delay_minutes_2} minutes")

if delay_minutes_2 > 0:
    print("  Result: This trip is delayed.")

print("  (No output above = condition was False = "
      "trip is on time)")

# ─────────────────────────────────────────────────────
# SECTION 2 - IF-ELSE STATEMENT
# else handles the False path when if is not triggered
# Transit use: classify a trip as delayed or on time
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: if-else Statement ---")
print("Classifying trips as delayed or on time\n")

test_delays = [0, 3, 8, 22]

for delay in test_delays:
    print(f"Delay = {delay:>2} min  →  ", end="")
    if delay >= 5:
        print("DELAYED — log this trip for review")
    else:
        print("ON TIME — no action needed")

# ─────────────────────────────────────────────────────
# SECTION 3 - IF-ELIF-ELSE STATEMENT
# elif handles multiple distinct conditions
# Only the FIRST matching branch executes
# Transit use: classify delay severity into categories
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: if-elif-else Statement ---")
print("Classifying delay severity into categories\n")
print("Rules:")
print("  On Time      → delay < 5 minutes")
print("  Minor Delay  → delay 5 to 15 minutes")
print("  Major Delay  → delay 16 to 30 minutes")
print("  Severe Delay → delay > 30 minutes")
print()

sample_delays = [2, 8, 19, 35, 0, 15, 31, 5]

for delay in sample_delays:
    print(f"Delay = {delay:>2} min  →  ", end="")

    if delay < 5:
        status = "ON TIME"
        action = "No intervention needed"
    elif delay <= 15:
        status = "MINOR DELAY"
        action = "Monitor route performance"
    elif delay <= 30:
        status = "MAJOR DELAY"
        action = "Notify operations team"
    else:
        status = "SEVERE DELAY"
        action = "Immediate investigation required"

    print(f"{status:<15} | {action}")

# ─────────────────────────────────────────────────────
# SECTION 4 - LOGICAL OPERATORS
# and  → BOTH conditions must be True
# or   → AT LEAST ONE condition must be True
# not  → INVERTS the condition
# Transit use: peak hour + route combination checks
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Logical Operators ---")
print()

# AND operator — both must be True
print("Using AND — peak hour delay alert:")
print("(Only trigger if BOTH peak hour AND delay > 10)\n")

trips = [
    {"route": "Route_42", "hour": 8,  "delay": 17},
    {"route": "Route_15", "hour": 14, "delay": 18},
    {"route": "Route_7",  "hour": 9,  "delay": 4},
    {"route": "Route_23", "hour": 8,  "delay": 22},
]

peak_hours = [7, 8, 9, 17, 18, 19]

for trip in trips:
    is_peak = trip["hour"] in peak_hours
    has_delay = trip["delay"] > 10

    print(f"  {trip['route']} | hour={trip['hour']} | "
          f"delay={trip['delay']} min")
    print(f"    is_peak={is_peak} AND "
          f"has_delay={has_delay}")

    if is_peak and has_delay:
        print("    → PEAK HOUR DELAY ALERT triggered")
    else:
        print("    → No alert (condition not fully met)")
    print()

# OR operator — at least one must be True
print("Using OR — flag for review:")
print("(Trigger if delay > 25 OR route is Route_7)\n")

review_trips = [
    {"route": "Route_42", "delay": 28},
    {"route": "Route_7",  "delay": 6},
    {"route": "Route_15", "delay": 12},
    {"route": "Route_7",  "delay": 31},
]

for trip in review_trips:
    high_delay = trip["delay"] > 25
    is_problem_route = trip["route"] == "Route_7"

    print(f"  {trip['route']} | delay={trip['delay']} min")
    print(f"    high_delay={high_delay} OR "
          f"is_problem_route={is_problem_route}")

    if high_delay or is_problem_route:
        print("    → Flagged for manual review")
    else:
        print("    → No flag needed")
    print()

# NOT operator — inverts the condition
print("Using NOT — skip incomplete records:")
print()

records = [
    {"trip_id": "T001", "delay": 12,   "complete": True},
    {"trip_id": "T002", "delay": None, "complete": False},
    {"trip_id": "T003", "delay": 7,    "complete": True},
    {"trip_id": "T004", "delay": None, "complete": False},
]

for record in records:
    if not record["complete"]:
        print(f"  {record['trip_id']} → SKIPPED "
              f"(incomplete record)")
    else:
        print(f"  {record['trip_id']} → PROCESSED "
              f"(delay = {record['delay']} min)")

# ─────────────────────────────────────────────────────
# SECTION 5 - COMBINED REAL-WORLD LOGIC
# Putting it all together in a realistic scenario
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Combined Real-World Logic ---")
print("Full decision pipeline for a transit trip\n")

def evaluate_trip(route, hour, delay, day):
    """Evaluate a single transit trip and
    return recommended action."""

    print(f"Evaluating: {route} | {day} | "
          f"Hour {hour} | Delay {delay} min")

    # Step 1 — Check data completeness
    if delay is None:
        print("  → SKIP: missing delay data")
        return

    # Step 2 — Peak hour check
    peak = hour in [7, 8, 9, 17, 18, 19]

    # Step 3 — Classify delay severity
    if delay < 5:
        severity = "On Time"
    elif delay <= 15:
        severity = "Minor Delay"
    elif delay <= 30:
        severity = "Major Delay"
    else:
        severity = "Severe Delay"

    # Step 4 — Combined action decision
    if severity == "Severe Delay" and peak:
        action = "URGENT — peak hour severe delay"
    elif severity == "Major Delay" and peak:
        action = "HIGH — peak hour major delay"
    elif severity == "Severe Delay" and not peak:
        action = "MEDIUM — off-peak severe delay"
    elif severity in ["Minor Delay", "Major Delay"]:
        action = "LOW — standard delay logged"
    else:
        action = "NONE — trip on time"

    print(f"  Severity  : {severity}")
    print(f"  Peak Hour : {peak}")
    print(f"  Action    : {action}")
    print()

# Test with multiple trips
evaluate_trip("Route_42", 8,    34, "Monday")
evaluate_trip("Route_15", 14,   18, "Wednesday")
evaluate_trip("Route_7",  9,    None, "Friday")
evaluate_trip("Route_23", 18,   4,  "Tuesday")
evaluate_trip("Route_42", 17,   28, "Thursday")

print("=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.16 - Conditionals Verified")
print("=" * 57)