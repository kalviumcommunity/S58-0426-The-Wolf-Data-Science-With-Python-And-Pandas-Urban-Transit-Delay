# functions_transit.py
# Milestone 5.18 - Defining and Calling Python Functions
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate function definition, calling,
#          parameters, return values, and scope
#          using transit domain examples

print("=" * 57)
print("  MILESTONE 5.18 - DEFINING AND CALLING FUNCTIONS")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - DEFINING AND CALLING A BASIC FUNCTION
# def keyword defines the function
# Function name describes what it does
# Indented body contains the logic
# Transit use: print a welcome/header message
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Defining and Calling a Function ---")

def print_project_header():
    """Prints the project header for the analysis."""
    print("  ----------------------------------------")
    print("  Project  : Urban Transit Delay Analysis")
    print("  Author   : Abhishek")
    print("  Goal     : Identify peak delay patterns")
    print("  ----------------------------------------")

# Calling the function — executes the body
print("\nCalling print_project_header():")
print_project_header()

# Call it again — same result, no code duplication
print("\nCalling it again:")
print_project_header()

print("\nKey point: function defined ONCE, called TWICE")
print("No code duplication — this is the core benefit")

# ─────────────────────────────────────────────────────
# SECTION 2 - FUNCTION WITH PARAMETERS
# Parameters are variables listed in the definition
# Arguments are the actual values passed when calling
# Transit use: classify a single trip's delay
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Function with Parameters ---")

def classify_delay(delay_minutes):
    """Classify a trip delay into a severity category.

    Parameter:
        delay_minutes (int/float): delay in minutes
    """
    if delay_minutes < 5:
        return "On Time"
    elif delay_minutes <= 15:
        return "Minor Delay"
    elif delay_minutes <= 30:
        return "Major Delay"
    else:
        return "Severe Delay"

# Calling with different arguments
print("\nTesting classify_delay() with various inputs:")
test_delays = [2, 8, 19, 35, 0, 15, 31]

for delay in test_delays:
    result = classify_delay(delay)
    print(f"  classify_delay({delay:>2}) → {result}")

# ─────────────────────────────────────────────────────
# SECTION 3 - FUNCTION WITH MULTIPLE PARAMETERS
# Multiple parameters separated by commas
# Order of arguments must match parameter order
# Transit use: calculate delay for a trip
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Multiple Parameters ---")

def calculate_delay(scheduled_time, actual_time):
    """Calculate delay in minutes between two times.

    Parameters:
        scheduled_time (int): planned arrival in minutes
                              from midnight
        actual_time    (int): actual arrival in minutes
                              from midnight
    Returns:
        int: delay in minutes (0 if arrived early)
    """
    delay = actual_time - scheduled_time
    if delay < 0:
        return 0      # arrived early — no delay
    return delay

# Convert HH:MM to minutes from midnight for testing
# 08:00 = 8*60 = 480, 08:17 = 8*60+17 = 497
trips_to_check = [
    ("Route_42", 480, 497),     # 08:00 → 08:17
    ("Route_15", 465, 469),     # 07:45 → 07:49
    ("Route_7",  540, 562),     # 09:00 → 09:22
    ("Route_23", 525, 524),     # 08:45 → 08:44 early
]

print("\nCalculating delays for each trip:")
print(f"  {'Route':<12} {'Scheduled':<12} "
      f"{'Actual':<10} {'Delay'}")
print("  " + "-" * 42)

for route, sched, actual in trips_to_check:
    delay = calculate_delay(sched, actual)
    status = classify_delay(delay)
    print(f"  {route:<12} {sched:<12} "
          f"{actual:<10} {delay} min → {status}")

# ─────────────────────────────────────────────────────
# SECTION 4 - FUNCTION WITH DEFAULT PARAMETERS
# Default values used when argument not provided
# Transit use: compute stats with optional threshold
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Default Parameters ---")

def summarize_route(route_name, delays,
                    threshold=10):
    """Print a summary of delays for one route.

    Parameters:
        route_name (str)  : name of the route
        delays     (list) : list of delay values
        threshold  (int)  : alert threshold in minutes
                            default is 10
    """
    avg   = sum(delays) / len(delays)
    total = sum(delays)
    worst = max(delays)
    count = len(delays)
    above = sum(1 for d in delays if d > threshold)

    print(f"\n  Route    : {route_name}")
    print(f"  Trips    : {count}")
    print(f"  Avg delay: {avg:.1f} min")
    print(f"  Total    : {total} min")
    print(f"  Worst    : {worst} min")
    print(f"  Above {threshold} min: {above} trips")

    if avg > threshold:
        print(f"  Status   : NEEDS ATTENTION")
    else:
        print(f"  Status   : ACCEPTABLE")

# Call with default threshold (10)
print("\nUsing default threshold (10 min):")
summarize_route("Route_7",  [22, 31, 18, 25, 34])

# Call with custom threshold (20)
print("\nUsing custom threshold (20 min):")
summarize_route("Route_42", [14, 17, 20, 12, 19],
                threshold=20)

# ─────────────────────────────────────────────────────
# SECTION 5 - FUNCTION CALLING ANOTHER FUNCTION
# Functions can call other functions
# Keeps each function small and focused
# Transit use: full trip evaluation pipeline
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Functions Calling Functions ---")

def is_peak_hour(hour):
    """Check if a given hour is a peak travel hour.

    Parameter:
        hour (int): hour of day 0-23
    Returns:
        bool: True if peak hour, False otherwise
    """
    peak_hours = [7, 8, 9, 17, 18, 19]
    return hour in peak_hours

def get_alert_level(delay, hour):
    """Determine alert level for a trip.
    Calls classify_delay() and is_peak_hour()
    internally.

    Parameters:
        delay (int): delay in minutes
        hour  (int): hour of trip
    Returns:
        str: alert level description
    """
    severity = classify_delay(delay)    # calls Section 2
    peak     = is_peak_hour(hour)       # calls above

    if severity == "Severe Delay" and peak:
        return "CRITICAL — peak hour severe delay"
    elif severity == "Major Delay" and peak:
        return "HIGH     — peak hour major delay"
    elif severity == "Severe Delay":
        return "MEDIUM   — off-peak severe delay"
    elif severity in ["Minor Delay", "Major Delay"]:
        return "LOW      — standard delay"
    else:
        return "NONE     — on time"

# Test the combined pipeline
print("\nFull trip evaluation pipeline:")
eval_trips = [
    ("Route_42", 34, 8),
    ("Route_15", 18, 14),
    ("Route_7",  31, 17),
    ("Route_23",  2, 9),
    ("Route_56", 22, 11),
]

print(f"\n  {'Route':<12} {'Delay':<8} "
      f"{'Hour':<6} Alert Level")
print("  " + "-" * 52)

for route, delay, hour in eval_trips:
    alert = get_alert_level(delay, hour)
    peak_label = "peak" if is_peak_hour(hour) \
                 else "off-peak"
    print(f"  {route:<12} {delay:<8} "
          f"{hour}h ({peak_label:<8}) → {alert}")

# ─────────────────────────────────────────────────────
# SECTION 6 - FUNCTION SCOPE
# Variables defined inside a function are LOCAL
# They do not exist outside the function
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Function Scope ---")

# Global variable
project_name = "Urban Transit Delay Analysis"

def show_scope_demo():
    """Demonstrate local vs global variable scope."""
    local_var = "I exist only inside this function"
    print(f"  Inside function:")
    print(f"    local_var    = {local_var}")
    print(f"    project_name = {project_name}")
    # project_name is global — readable inside function

show_scope_demo()

print(f"\n  Outside function:")
print(f"    project_name = {project_name}")
print(f"    local_var    = ", end="")

try:
    print(local_var)
except NameError as e:
    print(f"NameError — {e}")
    print("    local_var does not exist outside "
          "the function")

print("\n  Scope rule: variables defined inside a")
print("  function are LOCAL — they cannot be")
print("  accessed from outside the function.")
print("  This prevents accidental data modification.")

# ─────────────────────────────────────────────────────
# SECTION 7 - REAL PIPELINE USING ALL FUNCTIONS
# Putting everything together
# ─────────────────────────────────────────────────────

print("\n--- SECTION 7: Complete Analysis Pipeline ---")
print("Processing all routes using defined functions\n")

all_route_data = {
    "Route_7" : {"delays": [22, 31, 18, 25, 34],
                 "peak_trips": 3},
    "Route_15": {"delays": [4,  3,  6,  2,  5],
                 "peak_trips": 5},
    "Route_42": {"delays": [14, 17, 20, 12, 19],
                 "peak_trips": 4},
    "Route_23": {"delays": [1,  2,  3,  1,  2],
                 "peak_trips": 5},
}

worst_route = None
worst_avg   = 0

for route, data in all_route_data.items():
    delays = data["delays"]
    avg    = sum(delays) / len(delays)
    status = classify_delay(avg)      # reusing function

    print(f"  {route}: avg = {avg:.1f} min "
          f"→ {status}")

    if avg > worst_avg:
        worst_avg   = avg
        worst_route = route

print(f"\n  Most problematic route: {worst_route}")
print(f"  Average delay         : {worst_avg:.1f} min")
print(f"  Recommendation        : Investigate "
      f"{worst_route} scheduling")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.18 - Functions Verified")
print("=" * 57)