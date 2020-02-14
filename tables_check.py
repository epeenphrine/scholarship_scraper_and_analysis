import json 
from connection import connect
import scholarships_parser as scholarships

## just checking if tables are working

with open("table_directories.json") as f:
    table_directories = json.load(f)

print(len(table_directories))

for directory in table_directories:
    soup = connect(directory)
    scholarships.get_scholarships(soup)