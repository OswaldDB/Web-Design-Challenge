import pandas as pd
import datetime

header_code = '<!DOCTYPE html>\r<html lang="en">\r<head>\r<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"/>\r    <meta charset="UTF-8">\r    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r<title>Document</title>\r</head>\r<body>\r\r'
nav_menu_code = '<!-- NavBar -->\r<nav class="navbar navbar-expand-lg navbar-light bg-light">\r<a class="navbar-brand">Climate Analysis</a>\r<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">\r<span class="navbar-toggler-icon"></span>\r</button>\r<div class="collapse navbar-collapse" id="navbarNavDropdown">\r<ul class="navbar-nav">\r<li class="nav-item active">\r<a class="nav-link" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/landing.html">Home <span class="sr-only">(current)</span></a>\r</li>\r<li class="nav-item">\r<a class="nav-link" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/data.html">Data Set</a>\r</li>\r<li class="nav-item">\r<a class="nav-link" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/comp.html">Comparative Analysis</a>\r</li>\r<li class="nav-item dropdown">\r<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Individual Analyses</a>\r<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r<a class="dropdown-item" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/vis_01.html">City Latitude vs. Max Temperature</a>\r<a class="dropdown-item" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/vis_02.html">City Latitude vs. Humidity</a>\r<a class="dropdown-item" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/vis_03.html">City Latitude vs. Cloudiness</a>\r<a class="dropdown-item" href="https://oswalddb.github.io/Web-Design-Challenge/WebVisualizations/HTML/vis_04.html">City Latitude vs. Wind Speed</a>\r</div>\r</li>\r</ul>\r</div>\r</nav>\r'
footer_code = '\r\r<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>\r<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\r<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>\r</body>\r</html>'

df = pd.read_csv("cities.csv")
df['City'] = df['City'].str.capitalize()
df['Date'] = pd.to_datetime(df['Date'], unit='s')
df = df[['City','Country','Lat','Lng','Date','Cloudiness','Humidity','Max Temp','Wind Speed']]

html_obj = df.to_html()
html_obj = header_code + nav_menu_code + html_obj + footer_code
Html_file = open("HTML/data.html","w")
Html_file.write(html_obj)
Html_file.close()




