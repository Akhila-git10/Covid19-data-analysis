import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_covid_data.csv')  #read csv
#print(df)

global_confirmed = df.groupby('date')['confirmed'].sum()  #confirmed cases for that particular day
#print(global_confirmed)

plt.figure(figsize=(12,6)) #figure=container , inches width=12 , height =6
plt.plot(global_confirmed.index , global_confirmed.values , marker='o' , linestyle='-')
plt.title('Global Confirmed COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Confirmed Cases')
plt.grid(True)
plt.xticks(rotation=45) #clearer x axis labels to read
plt.tight_layout()
plt.show()