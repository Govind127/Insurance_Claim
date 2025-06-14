# Insurance_Claim
This project tells about the data which was insurance data. It had three columns : Age, Affordibility and Bought_insurance. I've perfromed K-means Clustering on this data to cluster the data with similar category in three clusters.

🔍 PROJECT ANALYSIS – Insurance Dataset (Unsupervised Clustering)
✅ 1. Dataset Overview
Total Records: 28 customers

Features (Columns): 3

age: Customer's age (numerical)

affordibility: Whether they can afford insurance (0 = No, 1 = Yes)

bought_insurance: Whether they actually bought insurance (0 = No, 1 = Yes)

✅ All columns are numerical and contain no missing values — so the dataset is clean and ready for analysis.

✅ 2. Column-Wise Analysis
🔸 a) Age
Range: 18 to 62 years

Mean Age: ~39.89 years

Distribution: Fairly wide, from young adults to senior citizens.

Use: Critical for risk assessment and pricing.

🔸 b) Affordibility
Type: Binary (0 or 1)

Meaning:

0 → Cannot afford insurance

1 → Can afford insurance

Observation:

~68% of people marked as affordable (mean = 0.678).

🔸 c) Bought Insurance
Type: Binary (0 or 1)

Insight:

50% of people in the dataset actually bought insurance.

It allows us to model behavior and find what kind of people actually buy even if they can afford.

✅ 3. Statistical Summary (Key Metrics)
Feature	Min	Max	Mean	25%	50% (Median)	75%
Age	18	62	39.89	25	45.5	54.25
Affordibility	0	1	0.68	0	1	1
Bought Insurance	0	1	0.50	0	0.5	1

✅ 4. Patterns & Insights
Many young customers (<30) still bought insurance even if affordability was low — suggests interest/need.

Some older people who can afford didn’t buy — possibly due to low perceived benefit or other factors.

There might be an interaction between age and affordability affecting the purchase decision.

✅ 5. What Can You Do With This Dataset?
🔷 a) K-Means Clustering Use Case
Since bought_insurance is present but not always reliable, we can use K-Means Clustering to:

Segment customers into potential buyers, non-buyers, and maybe buyers.

Identify hidden clusters like:

Young & affordable but didn’t buy

Old & affordable who bought

Middle-aged with mid-affordibility

🔷 b) Model Recommendation
You can extend this into:

Logistic Regression to predict purchase behavior

Clustering to understand different customer groups

🎯 Final Summary:
“My dataset contains age, affordability, and insurance purchase status of 28 individuals. It’s clean and has no missing values. I found that while affordability influences purchase, some people still buy insurance without affordability — especially younger individuals. I used this data to run K-Means Clustering to find natural groupings in the data based on age and affordability, helping to identify customer segments and predict future insurance buyers. This is useful for targeted marketing and customer profiling in insurance companies.”
