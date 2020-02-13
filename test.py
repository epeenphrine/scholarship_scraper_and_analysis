#standard and pip install
import numpy as np
import json 

#non standard and non pip install
import scholarships_parser as scholarships
from connection import connect
from config import url
from proxyscrape import proxyscrape as scrape
import time
import os
import json

soup = connect(url)

soup = connect(url) ## single soup object
soup_pool = [] ## list of soup objects
soup_puddle = [] ## a nested list of soup objects

directories_dict = scholarships.get_directories_dict(soup) ## starts here to try to get all directories from the site 
directories = scholarships.get_directories(directories_dict)
for directory in directories:
    soup_pool.append(connect(directory))

for soup in soup_pool:
    directories_dict = scholarships.get_directories_dict(soup, directories_dict)



soup_pool = []
print(directories)
#for directory in directories:
#    soup_pool.append(connect(directory))
#for soup in soul_pool:
#    scholarships.get_scholarships(soup)

print('\n')
print('*************************************')


#for url in initial_directories:
#    soup_pool.append(connect(url))
#for soup1 in soup_pool:
#    soup_puddle.append(scholarships_parser.get_directories(soup1))
#
#checking = []
#for items in soup_puddle:
#    for item in items:
#        if item not in checking:
#            checking.append(item)
#
#for item in checking:
#    print (item)
#
#print(f"total : {len(checking)}")
#x = np.array(checking)
#print(f"unique : {len(np.unique(x))}")
#
###scholarship tables
#for url in checking:
#    try:
#        soup = connect(url)
#        print(url)
#        scholarships_parser.get_scholarships(soup)
#    except:
#        print("no table")
#scholarships_parser.get_scholarships(soup)
