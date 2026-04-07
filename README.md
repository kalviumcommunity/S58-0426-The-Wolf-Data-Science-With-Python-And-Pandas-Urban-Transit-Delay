# Urban Transit Delay Analysis
## Milestone 5.3 — Understanding the Data Science Lifecycle: 
## Question → Data → Insight

---

### Part A — Explaining the Lifecycle

#### 1. Starting with a Clear Question

The most important step in any data science project is not writing 
code or building models — it is defining a clear, specific question 
before touching any data.

This matters because data is just raw information. Without a question 
guiding you, you can spend hours exploring a dataset and still not 
know what you were looking for or whether you found anything useful. 
A vague question like "what is interesting in this data?" leads to 
vague answers that nobody can act on.

A good question is specific, measurable, and tied to a real decision. 
For example — "Which bus routes in the city have the highest average 
delay during morning peak hours?" is a question that points directly 
at what data you need, what analysis to run, and what a useful answer 
looks like.

The question also protects you from wasting time. If someone asks you 
to "just explore the data and see what comes out", you risk building 
visualizations and running analyses that look busy but answer nothing. 
Every step in data science should trace back to the original question.

---

#### 2. Data as Evidence

Once you have a clear question, data becomes your evidence — not your 
starting point. The question tells you what data you actually need, 
where to get it, and what quality it needs to be.

Understanding data before analyzing it means checking whether the data 
can actually answer your question. This involves looking at what columns 
exist, what time period the data covers, how complete it is, whether 
values are trustworthy, and whether the data represents what it claims 
to represent.

For example, if your question is about bus delays but the dataset only 
records whether a bus departed — not whether it arrived on time — then 
the data cannot answer your question regardless of how good your 
analysis is. Discovering this early saves enormous amounts of time.

Understanding data also means knowing its limitations. Real-world data 
is messy, incomplete, and sometimes wrong. A data scientist who skips 
this step builds analysis on a broken foundation — and the results will 
be wrong even if the code runs perfectly.

---

#### 3. How Insights Emerge from Exploration

Insights do not come from running code or making charts. They come from 
asking why — from noticing a pattern and questioning what it means in 
the real world.

A number like "Route 42 has an average delay of 18 minutes" is not an 
insight. An insight is: "Route 42 consistently delays by 18+ minutes 
between 8am and 10am on weekdays, which coincides with a school zone 
and a railway crossing — suggesting that infrastructure, not bus 
frequency, is the root cause."

That insight came from exploration — looking at patterns across time, 
route, and location — combined with judgment about what the numbers 
mean for real people. It is useful because someone can act on it. They 
can redesign the route, adjust the schedule, or raise it with the city 
council.

This is why insights emerge from exploration, not just from tools. The 
tool produces the number. The data scientist produces the meaning.

---

### Part B — Applying the Lifecycle to a Project Context

**Project: Urban Transit Delay Analysis**

#### The Question
Which bus routes in the city experience the highest and most consistent 
delays during morning and evening peak hours, and what patterns explain 
these delays?

This question is specific — it targets particular routes, particular 
time windows, and asks for patterns, not just averages. A transport 
authority can use this to make scheduling and infrastructure decisions.

#### The Data Needed
- Historical trip logs with scheduled departure/arrival times and 
  actual departure/arrival times
- Route identifiers, stop locations, and timestamps
- Day of week and date to distinguish weekday vs weekend patterns
- Ideally: weather data and traffic incident logs to cross-reference 
  delay causes

This data would come from the transit authority's operations database 
or from open public transport datasets such as GTFS feeds. It 
represents every trip that ran — when it was supposed to run versus 
when it actually ran.

#### The Useful Insight
A useful insight for this project would be: identifying the top 5 
routes with recurring delays above 10 minutes during 7am–10am on 
weekdays, along with the specific stops where delays consistently 
begin. This tells the authority exactly where to intervene — not just 
that delays exist, but where they start and when they are worst.

This is actionable. A manager can look at this and immediately know 
which routes to prioritize, which stops to investigate, and whether 
the problem is getting better or worse over time.

---

### Scenario Response

**Scenario: Dataset with no problem statement, teammate wants to 
immediately build visualizations and models.**

My response using the Question → Data → Insight framework:

I would pause the analysis and first establish a clear question. 
Without a problem statement, any visualization or model we build is 
essentially guessing — we might find something interesting by luck, 
but we cannot know if it is useful or relevant to any real decision.

The risk of skipping the question step is significant. We could spend 
days building a model that predicts something nobody needs predicted. 
We could build 20 charts that all show the same thing from different 
angles without a single actionable finding. We could also mislead 
stakeholders by presenting patterns that look meaningful but have no 
real-world significance.

What I would do first is ask: who is this data for and what decision 
are they trying to make? Even a rough answer — "the operations team 
wants to reduce delays" — gives enough direction to form a question.

Then I would inspect the data briefly to understand what it contains, 
what time period it covers, and whether it has the columns needed to 
answer that question.

Only after that would I build any visualizations — and each one would 
be designed to answer a specific part of the question, not just to 
"see what comes out."

This approach does not slow the work down. It makes the work count.