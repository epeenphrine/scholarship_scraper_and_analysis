import re 
from connection import connect 

base_url = 'https://scholarships.com'

def get_directories(soup):
    search = soup.findAll('a', href=True)
    directories = []
    directories_name = []
    file_paths = []
    for a in search:
        text = a.get_text(strip=True)
        href = a['href']
        if re.match(r"^/financial-aid/", href):
            print(text)
            print("\n")
            print(href)
            directories_name.append(text)
            file_paths.append(f' {base_url} {a["href"]}')
    
    print(file_paths)

    for file_path in file_paths:
        soup = connect(file_path)
        get_directories(soup)

