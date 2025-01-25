import pandas as pd
import plotly.express as px

# Load the dataset
file_path = r'C:/Users/skcod/OneDrive/Desktop/Bigdata project/crimedata.csv'  # Update the file path
df = pd.read_csv(file_path)

# Display column names
print("Column names in the dataset:", df.columns)

# Clean and select relevant data
df_cleaned = df[['District', '2019', '2020', '2021']]  # Only keep relevant columns
df_cleaned = df_cleaned.dropna()  # Remove rows with missing values if any
df_cleaned[['2019', '2020', '2021']] = df_cleaned[['2019', '2020', '2021']].apply(pd.to_numeric)  # Ensure numeric

# Prepare data for Plotly (long format for grouping by district and year)
df_long = df_cleaned.melt(id_vars='District', var_name='Year', value_name='Crimes')

# Create an interactive stacked bar chart using Plotly
fig = px.bar(
    df_long,
    x='Year',
    y='Crimes',
    color='District',
    title='Interactive Crime Trends by District (2019-2021)',
    labels={'Crimes': 'Total Number of Crimes', 'Year': 'Year'},
    hover_name='District',  # Show district name on hover
    text_auto=True  # Display crime numbers on the bars
)

# Customize layout for better readability
fig.update_layout(
    title_font_size=20,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    legend_title_font_size=14,
    legend=dict(title="District", orientation="v", x=1.05, y=1),  # Place legend outside
    margin=dict(t=50, l=50, r=50, b=50),
    plot_bgcolor="white"
)

# Show the interactive plot
fig.show()
