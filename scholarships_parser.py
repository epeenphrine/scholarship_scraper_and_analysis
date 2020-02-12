import re 
from connection import connect 
import time 
import json
all_directories = []
base_url = 'https://scholarships.com'
def get_directories(soup):
    global all_directories
    search = soup.findAll('a', href=True)
    directories = []
    directories_name = []
    for a in search:
        text = a.get_text(strip=True)
        href = a['href']
        if re.match(r"^/financial-aid/college-scholarships/scholarship-directory/", href):
            if str(href) not in all_directories:
                print('write')
                directories_name.append(text)
                directories.append(f'{base_url}{a["href"]}')
                all_directories.append(f'{base_url}{a["href"]}')
                print(all_directories)                     
    return soup_pool(directories, all_directories)

def soup_pool(directories, all_directories):
    soup_pool = []
    count = 0 
    length = len(directories)
    for directory in directories:
        count += 1
        print(directory)
        soup_pool.append(connect(directory))
        print(f"\n ******************************************************************* ")
        print(f"{count} / {length}")
        print("sleeping 5")
        
        for soup in soup_pool:
            time.sleep(5)
            get_directories(soup)