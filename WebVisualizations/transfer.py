import pandas as pd
import datetime

df = pd.read_csv("cities.csv")
df['City'] = df['City'].str.capitalize()

df['Date'] = pd.to_datetime(df['Date'], unit='s')

html_obj = df.to_html()
Html_file = open("HTML/data.html","w")
Html_file.write(html_obj)
Html_file.close()