import pandas as pd
import re

base_url = "https://scholarships.com"

def directories(directories_dict):
    directories = []
    for directory in directories_dict:
        for value in directory.items():
            directories.append(value)
    return directories

def get_title(directories_dict):
    titles = []
    for directory in directories_dict:
        for key in directory.items():
            titles.append(key)
    return titles
    

def get_directories(soup):
    directories_dict = []
    for a in soup.findAll('a', href=True):
        title = a.get_text(strip=True)
        href = a['href']
        if re.match(r"^/financial-aid/college-scholarships/scholarship-directory/", href):
            constructed_url = f"{base_url}{href}"
            directories_dict.append({ title : constructed_url })
    return directories_dict

def get_scholarships(soup):
    df = pd.read_html(str(soup))
    df = df[0]
    print(df)
    return data_clean(df)

def data_clean(df): 
    #remove , and $ in column
    
    df = df[df['Amount'] != "Varies"]
    df['amount_cleaned'] = df['Amount'].str.replace(',','')
    df['amount_cleaned'] = df['amount_cleaned'].str.replace('$', '')
    df['amount_cleaned'] = df['amount_cleaned'].str.replace('$', '')
    #df['amount_cleaned'] = pd.to_numeric(df['amount_cleaned']) 
    df['amount_cleaned'] = df['amount_cleaned'].astype(int)
    average_amount = df['amount_cleaned'].mean(axis=0)
    print(f" average : ${average_amount} ") 