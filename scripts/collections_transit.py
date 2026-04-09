# collections_transit.py
# Milestone 5.15 - Working with Python Lists, Tuples, Dictionaries
# Project: Urban Transit Delay Analysis
# Author: Abhishek
# Purpose: Demonstrate Python collection data structures
#          using transit domain examples

print("=" * 57)
print("  MILESTONE 5.15 - LISTS, TUPLES, AND DICTIONARIES")
print("  Urban Transit Delay Analysis")
print("=" * 57)

# ─────────────────────────────────────────────────────
# SECTION 1 - PYTHON LISTS
# Lists are ORDERED and MUTABLE
# - Ordered   : items maintain their position
# - Mutable   : items can be added, removed, changed
# Transit use : storing delay records, route lists,
#               stop sequences that may change
# ─────────────────────────────────────────────────────

print("\n--- SECTION 1: Python Lists ---")
print("Lists are ordered and mutable (changeable)")
print()

# Creating a list of delay values in minutes
delay_records = [14, 22, 5, 31, 8, 19, 3, 27, 11, 16]
print(f"Delay records        : {delay_records}")
print(f"Type                 : {type(delay_records)}")
print(f"Total items          : {len(delay_records)}")

# Accessing elements using index (starts at 0)
print(f"\nIndexing:")
print(f"  First delay        : {delay_records[0]} min "
      f"(index 0)")
print(f"  Last delay         : {delay_records[-1]} min "
      f"(index -1)")
print(f"  Third delay        : {delay_records[2]} min "
      f"(index 2)")

# Slicing
print(f"\nSlicing:")
print(f"  First 3 delays     : {delay_records[:3]}")
print(f"  Last 3 delays      : {delay_records[-3:]}")
print(f"  Middle section     : {delay_records[3:7]}")

# Modifying a list — this is what makes lists mutable
print(f"\nModifying the list:")
print(f"  Before change      : {delay_records}")
delay_records[0] = 12          # update first item
print(f"  After update [0]   : {delay_records}")

delay_records.append(9)        # add new delay record
print(f"  After append(9)    : {delay_records}")

delay_records.remove(31)       # remove the 31 min outlier
print(f"  After remove(31)   : {delay_records}")

delay_records.sort()           # sort in ascending order
print(f"  After sort()       : {delay_records}")

# List of route names — strings in a list
route_names = [
    "Route_7", "Route_15", "Route_23",
    "Route_42", "Route_56"
]
print(f"\nRoute names list     : {route_names}")
print(f"  Second route       : {route_names[1]}")
print(f"  Routes count       : {len(route_names)}")

# When to use a list
print("\nWhen to use a LIST:")
print("  Use lists when the data may change over time")
print("  e.g. delay records grow as new trips come in")
print("  e.g. route list changes when new routes added")

# ─────────────────────────────────────────────────────
# SECTION 2 - PYTHON TUPLES
# Tuples are ORDERED and IMMUTABLE
# - Ordered   : items maintain their position
# - Immutable : items CANNOT be changed after creation
# Transit use : GPS coordinates, fixed config values,
#               column name definitions
# ─────────────────────────────────────────────────────

print("\n--- SECTION 2: Python Tuples ---")
print("Tuples are ordered and immutable (fixed)")
print()

# GPS coordinates — should never change accidentally
depot_location = (28.6139, 77.2090)
terminal_a = (28.7041, 77.1025)
terminal_b = (28.5355, 77.3910)

print(f"Depot GPS            : {depot_location}")
print(f"Terminal A GPS       : {terminal_a}")
print(f"Terminal B GPS       : {terminal_b}")
print(f"Type                 : {type(depot_location)}")

# Accessing tuple elements
print(f"\nAccessing tuple elements:")
print(f"  Depot latitude     : {depot_location[0]}")
print(f"  Depot longitude    : {depot_location[1]}")

# Fixed column names for the dataset
dataset_columns = (
    "trip_id", "route_id", "scheduled_time",
    "actual_time", "delay_minutes", "day_of_week"
)
print(f"\nDataset columns tuple:")
for i, col in enumerate(dataset_columns):
    print(f"  [{i}] {col}")

# Demonstrating immutability
print("\nImmutability demonstration:")
print("  Attempting to change depot_location[0]...")
try:
    depot_location[0] = 29.0
except TypeError as e:
    print(f"  TypeError caught: {e}")
    print("  This is correct — tuples protect fixed data")

# Tuple unpacking
lat, lon = depot_location
print(f"\nTuple unpacking:")
print(f"  lat = {lat}, lon = {lon}")

# When to use a tuple
print("\nWhen to use a TUPLE:")
print("  Use tuples for data that must not change")
print("  e.g. GPS coordinates of fixed stations")
print("  e.g. column names of a standardized dataset")

# ─────────────────────────────────────────────────────
# SECTION 3 - PYTHON DICTIONARIES
# Dictionaries store KEY-VALUE pairs
# - Ordered   : maintains insertion order (Python 3.7+)
# - Mutable   : values can be changed, keys added
# - Key-based : access by meaningful name, not index
# Transit use : route details, trip records, stats
# ─────────────────────────────────────────────────────

print("\n--- SECTION 3: Python Dictionaries ---")
print("Dictionaries store key-value pairs")
print()

# A single trip record as a dictionary
trip_record = {
    "trip_id"        : "TRP_001",
    "route_id"       : "Route_42",
    "day_of_week"    : "Monday",
    "scheduled_time" : "08:00",
    "actual_time"    : "08:17",
    "delay_minutes"  : 17,
    "status"         : "Minor Delay"
}

print("Trip record dictionary:")
for key, value in trip_record.items():
    print(f"  {key:<20}: {value}")

print(f"\nType                 : {type(trip_record)}")

# Accessing values using keys
print(f"\nKey-based access:")
print(f"  Route ID           : {trip_record['route_id']}")
print(f"  Delay              : "
      f"{trip_record['delay_minutes']} minutes")
print(f"  Status             : {trip_record['status']}")

# Modifying dictionary values
print(f"\nModifying dictionary:")
print(f"  Before status      : {trip_record['status']}")
trip_record["delay_minutes"] = 20
trip_record["status"] = "Severe Delay"
print(f"  After update       : delay = "
      f"{trip_record['delay_minutes']} min, "
      f"status = {trip_record['status']}")

# Adding a new key
trip_record["weather"] = "Rain"
print(f"  New key added      : weather = "
      f"{trip_record['weather']}")

# Route summary dictionary
route_summary = {
    "Route_7"  : {"avg_delay": 21.5, "trips": 48,
                  "status": "Critical"},
    "Route_15" : {"avg_delay": 4.0,  "trips": 62,
                  "status": "Good"},
    "Route_42" : {"avg_delay": 16.3, "trips": 55,
                  "status": "Poor"},
    "Route_23" : {"avg_delay": 2.0,  "trips": 70,
                  "status": "Excellent"},
}

print("\nRoute summary (nested dictionary):")
for route, info in route_summary.items():
    print(f"  {route}: avg={info['avg_delay']} min | "
          f"trips={info['trips']} | "
          f"status={info['status']}")

# When to use a dictionary
print("\nWhen to use a DICTIONARY:")
print("  Use dicts when data has named fields")
print("  e.g. a trip record with route, time, delay")
print("  e.g. per-route statistics with multiple metrics")

# ─────────────────────────────────────────────────────
# SECTION 4 - CHOOSING THE RIGHT STRUCTURE
# ─────────────────────────────────────────────────────

print("\n--- SECTION 4: Choosing the Right Structure ---")
print()
print(f"  {'Structure':<12} {'Mutable':<10} "
      f"{'Access By':<12} {'Best For'}")
print(f"  {'-'*12} {'-'*10} {'-'*12} {'-'*25}")
print(f"  {'List':<12} {'Yes':<10} {'Index':<12} "
      f"Ordered, changeable data")
print(f"  {'Tuple':<12} {'No':<10} {'Index':<12} "
      f"Fixed, protected data")
print(f"  {'Dictionary':<12} {'Yes':<10} {'Key':<12} "
      f"Named fields, records")

print("\nIn this project:")
print("  LIST   → delay_records[] grows as trips come in")
print("  TUPLE  → dataset_columns fixed, never changes")
print("  DICT   → trip_record{} stores named trip fields")

print("\n" + "=" * 57)
print("  SCRIPT COMPLETED SUCCESSFULLY")
print("  Milestone 5.15 - Collections Verified")
print("=" * 57)