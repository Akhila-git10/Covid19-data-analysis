import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_covid_data.csv')

df['date'] = pd.to_datetime(df['date'])
print(df['date'])