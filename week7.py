import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df['species'] = iris_data.target_names[iris_data.target]

# Display the first few rows
print(iris_df.head())

# Check data types and missing values
print(iris_df.info())
print(iris_df.isnull().sum())

# Drop rows with missing values (if any)
iris_df.dropna(inplace=True)
# Compute basic statistics
print(iris_df.describe())
# Group by species and compute the mean of each numerical column
mean_by_species = iris_df.groupby('species').mean()
print(mean_by_species)

# Hypothetical time data
time_periods = ['Week 1', 'Week 2', 'Week 3']
average_petal_length = [mean_by_species['petal length (cm)'].values]

plt.figure(figsize=(10, 5))
plt.plot(time_periods, average_petal_length[0], marker='o')
plt.title('Average Petal Length Over Time')
plt.xlabel('Time Period')
plt.ylabel('Average Petal Length (cm)')
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x=mean_by_species.index, y=mean_by_species['petal length (cm)'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(iris_df['petal length (cm)'], bins=10, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
