from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv
import numpy as np

page = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")

soup = bs(page.text,'html.parser')
info_table_star = soup.find('table')

temp_list= []
table_data = info_table_star.find_all('tr')


name_of_star = []
distance_from_earth =[]
Mass = []
Radius =[]
Lum = []

for tr in table_data:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

headers = ["name_of_star" , "distance_from_earth" , "Mass" , "Radius" , "Lum"]

for i in range(1,len(temp_list)):
    name_of_star.append(temp_list[i][1])
    distance_from_earth.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

stars_info = pd.DataFrame(list(zip(name_of_star,distance_from_earth,Mass,Radius,Lum)),
columns=['Star_name','distance_from_earth','Mass','Radius','Luminosity'])

stars_info.to_csv('data.csv')

