import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_covid_data.csv')  #read csv

latest_date = df['date'].max()  #latest date
#print(latest_date)

latest_data = df[df['date'] == latest_date]
#print(latest_data)

country_totals = latest_data.groupby('country')['confirmed'].sum()
#print(country_totals)

top_10 = country_totals.sort_values(ascending=False).head(10)
print(top_10)

plt.figure(figsize=(10,6))
plt.bar(top_10.index,top_10.values, color='skyblue')
plt.title('Top 10 Countries with Highest Confirmed COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()