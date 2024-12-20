# User Engagement Analysis

This repository contains the code and analysis for the User Engagement Analysis of a telecom dataset. The goal is to track user engagement using various metrics and provide insights to improve the Quality of Service (QoS) and user experience.

## Dataset

The dataset contains information about user sessions, including session duration, download and upload traffic, and application usage. Key columns include:
- `MSISDN/Number`: Unique identifier for customers
- `Bearer Id`: Session identifier
- `Dur. (ms)`: Session duration in milliseconds
- `Total DL (Bytes)`: Total download traffic in bytes
- `Total UL (Bytes)`: Total upload traffic in bytes
- Application-specific traffic columns (e.g., `Social Media DL (Bytes)`, `Google DL (Bytes)`, etc.)

## Analysis Steps

### Task 2.1 - Perform the Following Tasks

1. **Aggregate Engagement Metrics per Customer**:
   - Aggregated session frequency, total session duration, and total traffic (download and upload) per customer.
   - Reported the top 10 customers per engagement metric.

2. **Normalize Each Engagement Metric and Run K-Means Clustering**:
   - Normalized the engagement metrics.
   - Ran K-Means clustering with k=3 to classify customers into three groups of engagement.

3. **Compute Metrics for Each Cluster**:
   - Computed the minimum, maximum, average, and total non-normalized metrics for each cluster.
   - Interpreted the results visually with accompanying text.

4. **Aggregate User Total Traffic per Application**:
   - Aggregated user total traffic per application.
   - Derived the top 10 most engaged users per application.

5. **Plot the Top 3 Most Used Applications**:
   - Identified the top 3 most used applications.
   - Plotted the top 10 users for each of the top 3 applications using bar charts.

6. **Optimize the Value of k Using the Elbow Method**:
   - Used the elbow method to find the optimal value of k for K-Means clustering.
   - Interpreted the findings.

## Code

The code for the analysis is provided in the `User_Engagement_Analysis.ipynb` Jupyter Notebook. Key sections include:

### Aggregating Engagement Metrics

```python
# Aggregate engagement metrics per customer
engagement_metrics = df.groupby('MSISDN/Number').agg({
    'Bearer Id': 'count',  # Session frequency
    'Dur. (ms)': 'sum',    # Total session duration
    'Total DL (Bytes)': 'sum',  # Total download traffic
    'Total UL (Bytes)': 'sum'   # Total upload traffic
}).reset_index()

# Rename columns for clarity
engagement_metrics.rename(columns={
    'Bearer Id': 'session_frequency',
    'Dur. (ms)': 'total_duration',
    'Total DL (Bytes)': 'total_download',
    'Total UL (Bytes)': 'total_upload'
}, inplace=True)

# Calculate total traffic
engagement_metrics['total_traffic'] = engagement_metrics['total_download'] + engagement_metrics['total_upload']