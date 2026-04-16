# data_types_transit.py
# Milestone 5.14 - Understanding Python Numeric and String Data Types
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate numeric and string data types using
#          transit domain examples

# ─────────────────────────────────────────────────────
# SECTION 1 - INTEGER DATA TYPE
# Integers are whole numbers with no decimal point
# Used for: trip counts, route numbers, stop IDs
# ─────────────────────────────────────────────────────

print("=" * 55)
print("  MILESTONE 5.14 - PYTHON NUMERIC & STRING DATA TYPES")
print("  Urban Transit Delay Analysis")
print("=" * 55)

print("\n--- SECTION 1: Integer Data Type ---")

total_trips = 152          # number of trips recorded today
delayed_trips = 47         # trips with delay above 5 minutes
on_time_trips = 105        # trips that arrived on time
route_number = 42          # bus route identifier

print(f"Total trips today    : {total_trips}")
print(f"Delayed trips        : {delayed_trips}")
print(f"On time trips        : {on_time_trips}")
print(f"Route number         : {route_number}")
print(f"Type of total_trips  : {type(total_trips)}")

# Integer arithmetic
print("\nInteger Arithmetic:")
print(f"  Total check: {delayed_trips} + {on_time_trips} "
      f"= {delayed_trips + on_time_trips}")
print(f"  Difference : {total_trips} - {delayed_trips} "
      f"= {total_trips - delayed_trips}")
print(f"  Floor div  : {total_trips} // 10 "
      f"= {total_trips // 10} (groups of 10)")
print(f"  Modulo     : {total_trips} % 10 "
      f"= {total_trips % 10} (remainder)")

# ─────────────────────────────────────────────────────
# SECTION 2 - FLOAT DATA TYPE
# Floats are numbers with decimal points
# Used for: average delays, percentages, coordinates
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Float Data Type ---")

avg_delay = 12.7           # average delay in minutes
max_delay = 34.5           # maximum recorded delay
latitude = 28.6139         # GPS latitude of depot
longitude = 77.2090        # GPS longitude of depot
delay_rate = 47 / 152      # proportion of delayed trips

print(f"Average delay        : {avg_delay} minutes")
print(f"Maximum delay        : {max_delay} minutes")
print(f"Depot latitude       : {latitude}")
print(f"Depot longitude      : {longitude}")
print(f"Delay rate (raw)     : {delay_rate}")
print(f"Delay rate (rounded) : {round(delay_rate, 4)}")
print(f"Delay rate (percent) : {delay_rate * 100:.2f}%")
print(f"Type of avg_delay    : {type(avg_delay)}")

# Float arithmetic
print("\nFloat Arithmetic:")
print(f"  avg + 5.0  = {avg_delay + 5.0}")
print(f"  avg * 2    = {avg_delay * 2}")
print(f"  avg / 3    = {avg_delay / 3:.4f}")

# Important precision note
print("\nFloat Precision Note:")
print(f"  0.1 + 0.2  = {0.1 + 0.2}")
print(f"  This is a known float precision behavior in Python")
print(f"  Use round() to control decimal places: "
      f"{round(0.1 + 0.2, 2)}")

# ─────────────────────────────────────────────────────
# SECTION 3 - STRING DATA TYPE
# Strings are text data enclosed in quotes
# Used for: route names, station names, status labels
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: String Data Type ---")

route_name = "Route 42 - City Express"
station_name = "Central Bus Terminal"
delay_status = "Severe Delay"
day_of_week = "Monday"
direction = "Northbound"

print(f"Route name           : {route_name}")
print(f"Station name         : {station_name}")
print(f"Delay status         : {delay_status}")
print(f"Day                  : {day_of_week}")
print(f"Type of route_name   : {type(route_name)}")

# String operations
print("\nString Operations:")
print(f"  Uppercase  : {route_name.upper()}")
print(f"  Lowercase  : {route_name.lower()}")
print(f"  Length     : {len(route_name)} characters")
print(f"  Replace    : "
      f"{route_name.replace('Express', 'Local')}")
print(f"  Starts with 'Route': "
      f"{route_name.startswith('Route')}")
print(f"  Contains 'City'    : "
      f"{'City' in route_name}")

# String concatenation
print("\nString Concatenation:")
full_label = day_of_week + " | " + direction + \
             " | " + delay_status
print(f"  Combined label: {full_label}")

# f-string formatting
trip_summary = (f"Trip on {day_of_week}: "
                f"{route_name} — Status: {delay_status}")
print(f"  f-string   : {trip_summary}")

# ─────────────────────────────────────────────────────
# SECTION 4 - TYPE CONVERSION (SAFE MIXING)
# Converting between types intentionally
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Type Conversion ---")

# String to integer — route number from a data file
route_id_str = "42"
route_id_int = int(route_id_str)
print(f"String '42' to int   : {route_id_int} "
      f"— type: {type(route_id_int)}")

# String to float — delay value read from CSV
delay_str = "14.5"
delay_float = float(delay_str)
print(f"String '14.5' to float: {delay_float} "
      f"— type: {type(delay_float)}")

# Integer to string — for building labels
trip_count_str = str(total_trips)
label = "Total trips recorded: " + trip_count_str
print(f"Int to string label  : {label}")

# Float to string — for display
delay_label = "Average delay: " + str(avg_delay) + " min"
print(f"Float to string      : {delay_label}")

# ─────────────────────────────────────────────────────
# SECTION 5 - TYPE MISMATCH DEMONSTRATION
# Showing what happens when types are mixed incorrectly
# ─────────────────────────────────────────────────────

print("\n--- SECTION 5: Type Mismatch Example ---")

print("Attempting to add a string and integer directly...")
try:
    result = "Delay: " + 14
except TypeError as e:
    print(f"  TypeError caught: {e}")
    print(f"  Fix: convert int to str first")
    result = "Delay: " + str(14)
    print(f"  Corrected result : {result}")

print("\nType Awareness Summary:")
print(f"  route_number : {type(route_number)} — "
      f"use for calculations")
print(f"  avg_delay    : {type(avg_delay)} — "
      f"use for precise measurements")
print(f"  route_name   : {type(route_name)} — "
      f"use for labels and display")

print("\n" + "=" * 55)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.14 - Data Types Verified")
print("=" * 55)