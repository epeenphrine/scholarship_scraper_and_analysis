import scholarships_parser
from connection import connect 
from config import url
from proxyscrape import proxyscrape as scrape
import time
import os
import json

soup = connect(url)

scholarships_parser.get_directories(soup)

##soup_pool = scholarships_parser.get_directories2(directories)
##for soup in soup_pool:
    ##directories = scholarships_parser.get_directories(soup)
#scholarships_parser.get_directories(soup)