# functions_io_transit.py
# Milestone 5.19 - Passing Data into Functions
#                  and Returning Results
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate parameters, arguments,
#          return values, and composable function
#          design using transit domain examples

print("=" * 57)
print("  MILESTONE 5.19 - PASSING DATA AND RETURNING")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - PARAMETERS VS ARGUMENTS
# Parameter : variable name in the function definition
# Argument  : actual value passed when calling
# Transit   : pass route name and delay into a checker
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Parameters vs Arguments ---")
print()
print("  Definition  → parameter is the placeholder")
print("  Call        → argument is the actual value")
print()

def check_delay_status(route_name, delay_minutes):
    """Check and return the status of one trip.

    Parameters:
        route_name    (str)       : name of the route
        delay_minutes (int/float) : delay in minutes
    Returns:
        str: status string describing the trip
    """
    if delay_minutes < 5:
        status = "ON TIME"
    elif delay_minutes <= 15:
        status = "MINOR DELAY"
    elif delay_minutes <= 30:
        status = "MAJOR DELAY"
    else:
        status = "SEVERE DELAY"

    return f"{route_name} — {delay_minutes} min " \
           f"— {status}"

# Calling with different arguments each time
print("Calling check_delay_status() 4 times:")
print(f"  {check_delay_status('Route_42', 17)}")
print(f"  {check_delay_status('Route_15', 3)}")
print(f"  {check_delay_status('Route_7',  31)}")
print(f"  {check_delay_status('Route_23', 8)}")

print()
print("  Same function, different arguments each call")
print("  Parameters: route_name, delay_minutes")
print("  Arguments : 'Route_42' and 17, etc.")

# ─────────────────────────────────────────────────────
# SECTION 2 - RETURN STATEMENT
# return sends a value BACK to the caller
# Execution stops at return — nothing after runs
# Returning is better than printing inside a function
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: The return Statement ---")
print()

def calculate_average_delay(delay_list):
    """Calculate and return the average delay.

    Parameter:
        delay_list (list): list of delay values
    Returns:
        float: average delay rounded to 2 decimal places
    """
    if len(delay_list) == 0:
        return 0.0               # guard against empty list
    total   = sum(delay_list)
    average = total / len(delay_list)
    return round(average, 2)     # return, do not print

def calculate_max_delay(delay_list):
    """Return the maximum delay in a list.

    Parameter:
        delay_list (list): list of delay values
    Returns:
        int/float: maximum delay value
    """
    if len(delay_list) == 0:
        return 0
    return max(delay_list)

def calculate_min_delay(delay_list):
    """Return the minimum delay in a list.

    Parameter:
        delay_list (list): list of delay values
    Returns:
        int/float: minimum delay value
    """
    if len(delay_list) == 0:
        return 0
    return min(delay_list)

# Store returned values — reuse them later
route_7_delays = [22, 31, 18, 25, 34, 29, 20]

avg_delay = calculate_average_delay(route_7_delays)
max_delay = calculate_max_delay(route_7_delays)
min_delay = calculate_min_delay(route_7_delays)

print("Route_7 delay statistics:")
print(f"  Raw data  : {route_7_delays}")
print(f"  Average   : {avg_delay} min "
      f"← returned by calculate_average_delay()")
print(f"  Maximum   : {max_delay} min "
      f"← returned by calculate_max_delay()")
print(f"  Minimum   : {min_delay} min "
      f"← returned by calculate_min_delay()")
print()
print("  Note: functions RETURN values — the calling")
print("  code stores and uses them. No printing")
print("  inside the function itself.")

# ─────────────────────────────────────────────────────
# SECTION 3 - USING RETURNED VALUES IN CALCULATIONS
# Returned values can be stored, computed on,
# and passed into other functions
# Transit: chain function outputs through pipeline
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Using Returned Values ---")
print()

def calculate_delay_range(delay_list):
    """Return the range between max and min delay.

    Parameter:
        delay_list (list): list of delay values
    Returns:
        int/float: difference between max and min
    """
    return calculate_max_delay(delay_list) - \
           calculate_min_delay(delay_list)

def calculate_delay_rate(delayed_count, total_count):
    """Return the percentage of trips that were delayed.

    Parameters:
        delayed_count (int): number of delayed trips
        total_count   (int): total number of trips
    Returns:
        float: delay rate as a percentage
    """
    if total_count == 0:
        return 0.0
    return round((delayed_count / total_count) * 100, 1)

def classify_route_health(avg_delay):
    """Return a health label for a route based on avg.

    Parameter:
        avg_delay (float): average delay in minutes
    Returns:
        str: health classification label
    """
    if avg_delay < 5:
        return "Excellent"
    elif avg_delay < 10:
        return "Good"
    elif avg_delay < 20:
        return "Poor"
    else:
        return "Critical"

# Chain returned values through multiple functions
routes_data = {
    "Route_7" : [22, 31, 18, 25, 34],
    "Route_15": [4,  3,  6,  2,  5],
    "Route_42": [14, 17, 20, 12, 19],
    "Route_23": [1,  2,  3,  1,  2],
}

print("Route health report using chained functions:")
print()
print(f"  {'Route':<12} {'Avg':>6} {'Max':>6} "
      f"{'Min':>6} {'Range':>7} {'Health'}")
print("  " + "-" * 52)

for route, delays in routes_data.items():
    avg    = calculate_average_delay(delays)
    mx     = calculate_max_delay(delays)
    mn     = calculate_min_delay(delays)
    rng    = calculate_delay_range(delays)
    health = classify_route_health(avg)  # avg passed in

    print(f"  {route:<12} {avg:>6} {mx:>6} "
          f"{mn:>6} {rng:>7} {health}")

print()
print("  Each column value is a RETURNED result")
print("  passed into the next function or printed")

# ─────────────────────────────────────────────────────
# SECTION 4 - RETURNING MULTIPLE VALUES
# Python functions can return multiple values
# as a tuple — caller unpacks them
# Transit: return both value AND label together
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Returning Multiple Values ---")
print()

def analyze_trip(route, delay):
    """Analyze one trip and return multiple results.

    Parameters:
        route (str)  : route identifier
        delay (float): delay in minutes
    Returns:
        tuple: (route, delay, status, action)
    """
    if delay < 5:
        status = "On Time"
        action = "No action"
    elif delay <= 15:
        status = "Minor Delay"
        action = "Monitor"
    elif delay <= 30:
        status = "Major Delay"
        action = "Notify ops team"
    else:
        status = "Severe Delay"
        action = "Immediate review"

    return route, delay, status, action

# Unpack multiple returned values
test_trips = [
    ("Route_42", 17),
    ("Route_7",  34),
    ("Route_15",  4),
    ("Route_23", 22),
]

print("Unpacking multiple return values:")
print()
print(f"  {'Route':<12} {'Delay':>6}  "
      f"{'Status':<14} Action")
print("  " + "-" * 52)

for route, delay in test_trips:
    r, d, status, action = analyze_trip(route, delay)
    print(f"  {r:<12} {d:>5}m  "
          f"{status:<14} {action}")

# ─────────────────────────────────────────────────────
# SECTION 5 - COMMON MISTAKES AND CORRECT PATTERNS
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Common Mistakes vs Correct ---")
print()

# MISTAKE 1 — printing instead of returning
print("Mistake 1: printing inside function")
print("  (cannot reuse the result elsewhere)")
print()
print("  def get_avg_WRONG(delays):")
print("      avg = sum(delays) / len(delays)")
print("      print(avg)   ← cannot store this")
print()
print("  Correct version returns the value:")
print("  def get_avg_RIGHT(delays):")
print("      return sum(delays) / len(delays)")
print("      ← caller stores: avg = get_avg_RIGHT(d)")
print()

# MISTAKE 2 — hardcoding values inside function
print("Mistake 2: hardcoding values")
print()
print("  def check_WRONG(delay):")
print("      if delay > 10:      ← hardcoded 10")
print("          return 'Delayed'")
print()
print("  Correct version uses a parameter:")
print("  def check_RIGHT(delay, threshold=10):")
print("      if delay > threshold:  ← flexible")
print("          return 'Delayed'")
print()

# MISTAKE 3 — missing return in one branch
print("Mistake 3: missing return in a branch")
print()
print("  def classify_WRONG(delay):")
print("      if delay > 15:")
print("          return 'Major'")
print("      # else branch missing → returns None")
print()
print("  Correct version always returns:")
print("  def classify_RIGHT(delay):")
print("      if delay > 15:")
print("          return 'Major'")
print("      else:")
print("          return 'Minor'   ← always returns")
print()

# Demonstrate None return
def missing_return_demo(delay):
    """Intentionally missing else return."""
    if delay > 15:
        return "Major Delay"
    # no else — returns None implicitly

result = missing_return_demo(5)
print(f"  missing_return_demo(5)  → {result}")
print(f"  Type: {type(result)}")
print("  None is returned when no return is reached")

# ─────────────────────────────────────────────────────
# SECTION 6 - COMPLETE DATA PIPELINE
# All functions working together end to end
# ─────────────────────────────────────────────────────

print("\n--- SECTION 6: Complete Data Pipeline ---")
print()

def compute_route_summary(route_name, delay_list,
                          threshold=10):
    """Compute a complete summary dict for a route.

    Parameters:
        route_name (str)  : route identifier
        delay_list (list) : list of delay values
        threshold  (int)  : delay alert threshold
    Returns:
        dict: summary with all computed statistics
    """
    avg    = calculate_average_delay(delay_list)
    mx     = calculate_max_delay(delay_list)
    mn     = calculate_min_delay(delay_list)
    rng    = calculate_delay_range(delay_list)
    health = classify_route_health(avg)
    trips  = len(delay_list)
    above  = sum(1 for d in delay_list
                 if d > threshold)

    return {
        "route"       : route_name,
        "avg_delay"   : avg,
        "max_delay"   : mx,
        "min_delay"   : mn,
        "delay_range" : rng,
        "health"      : health,
        "total_trips" : trips,
        "above_thresh": above,
        "threshold"   : threshold,
    }

# Use returned dict downstream
print("Full pipeline — compute_route_summary():\n")

for route, delays in routes_data.items():
    summary = compute_route_summary(route, delays)

    print(f"  {summary['route']}:")
    print(f"    avg={summary['avg_delay']} min | "
          f"max={summary['max_delay']} min | "
          f"health={summary['health']}")
    print(f"    {summary['above_thresh']} of "
          f"{summary['total_trips']} trips above "
          f"{summary['threshold']} min threshold")
    print()

print("  Returned dict reused for display,")
print("  filtering, or passing to next function.")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.19 - Function I/O Verified")
print("=" * 57)