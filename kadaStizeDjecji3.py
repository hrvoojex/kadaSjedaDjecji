#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

urlProracun = 'http://www.mfin.hr/hr/izvrsenje-proracuna'

# Request web page with GET
response = requests.get(urlProracun, headers=headers)
print(response)

# Find a table and save all rows in a list
html_soup = BeautifulSoup(response.text, 'html.parser')
tableList = html_soup.find_all('table')
table = tableList[0]
tableRows = table.find_all('tr')

# Search for a string 'doplatak za djecu' in a row
for row in tableRows:
    if 'doplatak za djecu' in row.text:
        myRow = row.text

# Extract just a date from a searched row
myReg = r'\d+\.\S+\.'       # \d+ - any number one or more times,
reg = re.compile(myReg)     #  \. - point,
myDate = reg.search(myRow)  # \S - non-whitespace character
if myDate:
    print('Dječji sjeda: ', myDate.group())                      # \. - point
else:
    print('No match')




