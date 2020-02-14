#standard and pip install
import numpy as np
import time
import os
import pickle
import json

#non standard and non pip install
import scholarships_parser as scholarships
from connection import connect
from config import url
from proxyscrape import proxyscrape as scrape

soup = connect(url)

soup = connect(url) ## single soup object
soup_pool = [] ## list of soup objects

directories_dict = scholarships.get_directories_dict(soup) ## starts here to try to get all directories from the site 
directories = scholarships.get_directories(directories_dict)
for directory in directories:
    soup_pool.append(connect(directory))

for soup in soup_pool:
    directories_dict = scholarships.get_directories_dict(soup, directories_dict)

directories = scholarships.get_directories(directories_dict)

print(len(directories))
soup_pool = []
table_directories = []
for directory in directories:
    soup = connect(directory)
    try:
        scholarships.get_scholarships(soup)
        table_directories.append(directory)
     
    except:
        print('\nprobably no table in this url\n')
with open("table_directories.json", 'w') as f:
    json.dump(table_directories, f)
print('\n')
print('*************************************')