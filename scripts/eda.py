# eda.py
import matplotlib.pyplot as plt
import seaborn as sns

# Compute correlation matrix
corr_matrix = user_data[['total_duration', 'total_download', 'total_upload', 'total_data']].corr()

# Plotting the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Compute correlation matrix
corr_matrix = user_data[['total_duration', 'total_download', 'total_upload', 'total_data']].corr()

# Plotting the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Plotting session duration distribution
plt.figure(figsize=(10, 6))
sns.histplot(user_data['total_duration'], kde=True)
plt.title('Distribution of Total Session Duration per User')
plt.xlabel('Total Duration (Seconds)')
plt.ylabel('Frequency')
plt.show()
