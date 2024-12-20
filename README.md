# Telecom Data Analysis

This repository contains the analysis for User Overview and User Engagement of a telecom dataset. The goal is to track user engagement and provide insights to improve the Quality of Service (QoS) and user experience.

## Dataset

The dataset contains information about user sessions, including session duration, download and upload traffic, and application usage. Key columns include:
- `MSISDN/Number`: Unique identifier for customers
- `Bearer Id`: Session identifier
- `Dur. (ms)`: Session duration in milliseconds
- `Total DL (Bytes)`: Total download traffic in bytes
- `Total UL (Bytes)`: Total upload traffic in bytes
- Application-specific traffic columns (e.g., `Social Media DL (Bytes)`, `Google DL (Bytes)`, etc.)
- `Handset Manufacturer`: Manufacturer of the handset
- `Handset Type`: Type of the handset

## Analysis Steps

### Task 1 - User Overview Analysis

1. **Identify the Top 10 Handsets Used by Customers**:
   - Identified the top 10 handsets used by customers based on the `Handset Type` column.

2. **Identify the Top 3 Handset Manufacturers**:
   - Identified the top 3 handset manufacturers based on the `Handset Manufacturer` column.

3. **Identify the Top 5 Handsets per Top 3 Handset Manufacturer**:
   - For each of the top 3 manufacturers, identified the top 5 handsets used by customers.

4. **Aggregate User Behavior Information**:
   - Aggregated user behavior information including session frequency, session duration, download data, upload data, and total data volume.

5. **Handle Missing Values and Outliers**:
   - Replaced missing values with the mean and handled outliers by capping values at the 99th percentile.

6. **Variable Transformations**:
   - Segmented users into top five decile classes based on total session duration and computed total data per decile class.

7. **Basic Metrics Analysis**:
   - Analyzed basic metrics (mean, median, etc.) and computed dispersion parameters for each quantitative variable.

8. **Graphical and Bivariate Analysis**:
   - Visualized data using histograms and scatter plots to explore relationships between variables.

9. **Correlation Analysis**:
   - Computed a correlation matrix for application-specific data and interpreted the findings.

10. **Dimensionality Reduction**:
    - Performed Principal Component Analysis (PCA) to reduce data dimensions and interpreted the results.

### Task 2 - User Engagement Analysis

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


