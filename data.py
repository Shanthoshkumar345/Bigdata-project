import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset (replace this with the actual path to your crime data)
file_path = r'C:/Users/skcod/OneDrive/Desktop/Bigdata project/crimedata.csv'  # Update with your correct path
df = pd.read_csv(file_path)

# Step 2: Check the columns in the dataset to identify the correct name for the year columns
print("Column names in the dataset:", df.columns)

# Step 3: Remove unnecessary columns like '_id', 'Sl. No' that are not needed for analysis
df_cleaned = df[['District', '2019', '2020', '2021']]  # We only need the District and Year columns

# Step 4: Group data by 'District' and sum the crimes for each year (if needed)
district_crime_yearly = df_cleaned.set_index('District').T  # Transpose the dataframe so years are rows
district_crime_yearly.columns = district_crime_yearly.columns.str.strip()  # Clean up any extra spaces in column names

# Step 5: Visualize Crime Trends for Each District Over the Years
plt.figure(figsize=(12, 8))
district_crime_yearly.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Crime Trends in Districts (2019-2021)', fontsize=16)
plt.xlabel('District')
plt.ylabel('Total Number of Crimes')
plt.xticks(rotation=45)
plt.legend(title='Year')
plt.tight_layout()
plt.show()

# Step 6: Insights and Recommendations
district_crime_yearly_total = district_crime_yearly.sum(axis=1)
high_crime_districts = district_crime_yearly_total[district_crime_yearly_total > district_crime_yearly_total.mean()]
print(f"Districts with high crime rates (above average):\n{high_crime_districts}")

# Example Recommendations:
if high_crime_districts.any():
    print("Recommendation: Implement more law enforcement resources in high-crime districts.")
else:
    print("Recommendation: Continue monitoring crime trends for potential future interventions.")
