import pandas as pd
import datetime

bootstrap_header = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\r<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\r\r<div class="table-responsive table">\r\r'
bootstrap_footer = '\r\r</div>'

df = pd.read_csv("cities.csv")
df['City'] = df['City'].str.capitalize()

df['Date'] = pd.to_datetime(df['Date'], unit='s')

html_obj = df.to_html()
html_obj = bootstrap_header + html_obj + bootstrap_footer
Html_file = open("HTML/data.html","w")
Html_file.write(html_obj)
Html_file.close()


