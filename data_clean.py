import pandas as pd

#load csv file
df = pd.read_csv('covid_data.csv')
print(df.head())
print(df.tail())

#standardize column names
df.columns = df.columns.str.strip()     #remove spaces,tabs,new lines
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace( ' ' , '_')
print(df.columns)

#null and data type check
print(df.info())
(df.isnull().sum())

#convert date column to datetime
df['date'] = pd.to_datetime(df['date'] , errors='coerce')
print(df['date'])

#drop rows with missing dates and countries
df = df.dropna( subset = ['date' , 'country'])
df[['confirmed' , 'recovered' , 'deaths']] = df[['confirmed' , 'recovered' , 'deaths']].fillna(0)
print(df)

#sort data by date
df = df.sort_values('date')
print(df)

#save cleaned data
df.to_csv('cleaned_covid_data.csv' , index=False) #index false means extra index will not be added