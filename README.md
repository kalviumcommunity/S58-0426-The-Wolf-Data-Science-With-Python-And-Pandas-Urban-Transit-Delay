---

## Milestone 5.44 — Final Project Insights, Assumptions, and Limitations

---

### Project Overview

This project was built to answer one central question:
**Which bus routes experience the highest and most
consistent delays, during which time periods, and what
patterns explain these delays?**

The work progressed through 20 milestones — from
environment setup through data loading, cleaning,
standardization, statistical analysis, and finally
this documentation. Every script, notebook, and
dataset in this repository was built to serve that
one question.

---

### Key Project Insights

**Insight 1 — Route performance is highly unequal**

Analysis of delay_minutes across routes revealed that
Route_7 consistently averaged above 25 minutes of
delay per trip, while Route_23 averaged below 2
minutes. These are not random fluctuations — the
pattern held across multiple days and time periods.
This suggests structural differences between routes
such as road infrastructure, stop density, or
scheduling gaps rather than isolated incidents.

**Insight 2 — Peak hours amplify existing problems**

Trips operating between 7am–10am and 5pm–8pm showed
systematically higher delays than off-peak trips on
the same routes. Critically, routes that already
performed poorly off-peak became significantly worse
during peak hours. This indicates that high-delay
routes are not just slow — they are also more
sensitive to traffic volume, which compounds the
problem for the majority of commuters who travel
during peak windows.

**Insight 3 — Delay distributions are right-skewed**

For all routes, the mean delay was consistently higher
than the median delay. This right-skewed distribution
means that most trips are delayed by a moderate amount,
but a smaller number of trips experience extreme delays
that pull the average upward. The median is therefore
a more representative metric for the typical commuter
experience, while the mean better captures the total
delay burden on the system.

**Insight 4 — Service inconsistency is as harmful as
average delay**

Route_7 had not only the highest mean delay but also
the highest standard deviation — meaning commuters
could not predict whether they would be 20 minutes
late or 40 minutes late. High variability makes
journey planning impossible. Route_42 had moderate
average delay but lower variability, making it more
manageable from a commuter perspective despite
similar average numbers.

**Insight 5 — Missing data is concentrated in
supporting columns**

During data cleaning, missing values were found
primarily in passenger_count and hour_of_day — not
in the core analysis columns delay_minutes and
route_id. This means the missing data did not
fundamentally compromise delay analysis, though it
does limit the depth of passenger impact assessment.

---

### Assumptions

**Assumption 1 — Delay is defined as actual minus
scheduled arrival time**

Throughout this project, delay_minutes was calculated
as the difference between actual arrival time and
scheduled arrival time. This definition treats any
positive difference as a delay and any negative
difference (early arrival) as zero delay. Alternative
definitions — such as measuring from departure time
or including dwell time — were not explored.

**Assumption 2 — The sample dataset is representative**

The transit dataset used contains 40 trips across
4 routes over 5 days. This is a small sample that
was created to simulate realistic patterns. The
assumption that these patterns represent actual
system-wide behavior has not been validated against
real operational data. Conclusions should be treated
as directional rather than definitive.

**Assumption 3 — Missing values are missing at random**

When filling missing delay values with the median,
the assumption was that data was missing randomly —
not because extreme delays were systematically
excluded from recording. If the recording system
fails more often during high-delay periods, median
imputation would underestimate actual delay severity.

**Assumption 4 — Peak hours are fixed time windows**

Peak hours were defined as 7am–10am and 5pm–8pm
for all routes and all days. In reality, peak windows
may differ by route, direction, day of week, or
season. A more refined analysis would calculate peak
windows empirically from the data rather than
applying a fixed definition.

**Assumption 5 — Passenger count does not affect
delay**

The correlation analysis showed a weak relationship
between passenger_count and delay_minutes. The
project proceeded under the assumption that passenger
load is not a primary driver of delay. This assumption
simplifies the analysis but may not hold for routes
with frequent boarding and alighting at busy stops.

---

### Limitations

**Limitation 1 — Small sample size**

The dataset contains 40 trips across 4 routes over
5 days. This is insufficient to draw statistically
robust conclusions about long-term performance
patterns. Seasonal variation, public holidays,
special events, and weather conditions are completely
absent from this dataset. A production-grade analysis
would require at minimum 6–12 months of trip data
across all operating routes.

**Limitation 2 — No external factors included**

The analysis did not incorporate weather data,
traffic incident logs, road construction schedules,
or driver assignment records. In reality, a
significant proportion of transit delays are caused
by external factors outside the transport authority's
direct control. Without these covariates, the
analysis can identify where and when delays occur
but cannot explain why with confidence.

**Limitation 3 — No real-time data**

All data used in this project is historical and
batch-processed. The insights are retrospective —
they describe what happened, not what is currently
happening. A real-time monitoring system would
require streaming data infrastructure and live model
inference, which are outside the scope of this sprint.

**Limitation 4 — Binary peak hour classification**

The is_peak_hour flag was a binary True/False value
based on fixed time windows. This loses information
about how delay severity varies within peak windows
— for example, whether 8am is significantly worse
than 9am on Route_7. A continuous hour-of-day
analysis would provide more granular insight.

**Limitation 5 — No statistical significance testing**

Differences observed between routes and time periods
were not tested for statistical significance. The
observed differences may partially reflect sampling
variation rather than true systematic differences.
Formal hypothesis testing — such as t-tests for
delay differences between routes — would strengthen
the conclusions.

---

### What This Project Demonstrates

Despite its limitations, this project successfully
demonstrates the complete data science workflow:

| Stage | Milestone | Deliverable |
|---|---|---|
| Environment setup | 5.5 – 5.7 | Python, Conda, Jupyter verified |
| Python fundamentals | 5.13 – 5.19 | Scripts for data types, loops, functions |
| NumPy vectorization | 5.25 | Vectorized delay computations |
| Data loading | 5.29 | CSV loaded into Pandas DataFrames |
| Data inspection | 5.30, 5.32 | head, info, describe, indexing |
| Data cleaning | 5.33, 5.34 | Missing values detected and handled |
| Standardization | 5.36 | Column names and formats normalized |
| EDA | 5.37, 5.38 | Summary stats and distribution comparison |
| Documentation | 5.44 | This README |

The pipeline goes from raw messy data to clean
analyzed findings with every decision documented
and justified.

---

### Recommendations for Future Work

Based on the findings and limitations identified:

- Acquire at least 6 months of real operational
  trip data from a transit authority GTFS feed
- Incorporate weather and traffic incident data
  as covariates in delay modelling
- Build a route-level delay prediction model
  using Random Forest or Gradient Boosting
- Develop a Streamlit dashboard allowing transport
  planners to filter by route, hour, and day
- Conduct formal hypothesis testing to confirm
  whether route differences are statistically
  significant

---

### Video Walkthrough

[Click here to watch the final project video](PASTE_YOUR_LOOM_LINK_HERE)

---

### Repository Structure

S58-0426-The-Wolf-Data-Science-With-Python-And-Pandas-Urban-Transit-Delay/
│
├── data/
│   ├── raw/                  ← original unmodified data
│   └── processed/            ← cleaned and standardized data
│
├── notebooks/                ← exploratory Jupyter notebooks
│
├── scripts/                  ← all Python analysis scripts
│   ├── transit_analysis.py
│   ├── data_types_transit.py
│   ├── collections_transit.py
│   ├── conditionals_transit.py
│   ├── loops_transit.py
│   ├── functions_transit.py
│   ├── functions_io_transit.py
│   ├── vectorized_transit.py
│   ├── load_csv_transit.py
│   ├── inspect_dataframe_transit.py
│   ├── missing_values_transit.py
│   ├── handle_missing_transit.py
│   ├── standardize_transit.py
│   ├── indexing_slicing_transit.py
│   ├── summary_stats_transit.py
│   └── compare_distributions_transit.py
│
└── outputs/
├── figures/              ← charts and visualizations
└── reports/              ← summary reports

---

*Documentation written by Abhishek*
*Urban Transit Delay Analysis — Data Science Sprint*
*S58-0426 — The Wolf*