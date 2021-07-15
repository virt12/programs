
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import csv
site= "https://www.norwegian.com/uk/ipc/availability/avaday?D_City=OSLALL&A_City=FCO&D_Day=01&D_Month=202111&D_SelectedDay=01&R_Day=30&R_Month=202111&R_SelectedDay=30&AgreementCodeFK=-1&CurrencyCode=EUR&rnd=13274&processid=91353"
hdr = {'User-Agent': 'Morzilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = Request(site, headers=hdr)
try:
    page = urlopen(req)
except HTTPError as e:
    print(e.fp.read())
content = page.read()
soup=BeautifulSoup(content,'html.parser')
tags=soup.find_all('a')
page_body = soup.body
page_head = soup.head
find_by_class = soup.find_all(class_="label seatsokfare")
text = find_by_class[1]
text2=find_by_class[2]
text3=find_by_class[3]
text = str(find_by_class[1])
text2=str(find_by_class[2])
text3=str(find_by_class[3])
print(BeautifulSoup(text, "lxml").text)
print(BeautifulSoup(text2, "lxml").text)
print(BeautifulSoup(text3, "lxml").text)
a=BeautifulSoup(text, "lxml").text
b=BeautifulSoup(text2, "lxml").text
c=BeautifulSoup(text3, "lxml").text
print(a,b,c)
prices=[a,b,c]
fl = [float(x) for x in prices]
minpr=min(fl)
find_by_class2 = soup.find_all(class_="content emphasize")
text4=str(find_by_class2[0])
text5=str(find_by_class2[1])
arrival_time=BeautifulSoup(text4, "lxml").text
departure_time=BeautifulSoup(text5, "lxml").text
find_by_class3 = soup.find_all(class_="content")
text6=str(find_by_class3[12])
text7=str(find_by_class3[13])
arrival_airport=BeautifulSoup(text6, "lxml").text
departure_airport=BeautifulSoup(text7, "lxml").text
print(arrival_airport)
fields_values=[arrival_airport,departure_airport, arrival_time, departure_time, minpr]
fields = ['Arrival Airport', 'Departure Airporth', 'Arrival time', 'Departure time','Lowest price']
with open('C://Users//Žymantas/Desktop//travelings_compare7.csv', 'w', encoding='UTF8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerow(fields_values)



