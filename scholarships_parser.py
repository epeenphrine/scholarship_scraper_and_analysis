#standard and pip install
import pandas as pd
import re
import numpy as np

#non standard and non pip install
import scholarships_parser as scholarships
from connection import connect
from config import url


# used for constructing new url
base_url = "https://scholarships.com"

def get_directories(directories_dict):
    directories = []
    for title, directory in directories_dict.items():
        directories.append(directory)
    return directories

def get_title(directories_dict):
    titles = []
    for title, directory in directories_dict.items():
        titles.append(title)
    return titles
    
def get_directories_dict(soup, *args):
    if args:
        directories_dict = args[0]
        titles = []
        constructed_urls = []        
        for title, directory in directories_dict.items():
            titles.append(title)
            constructed_urls.append(directory)
    if not args:
        titles = []
        constructed_urls = []
    for a in soup.findAll('a', href=True):
        title = a.get_text(strip=True)
        href = a['href']
        if re.match(r"^/financial-aid/college-scholarships/scholarship-directory/", href):
            constructed_url = f"{base_url}{href}"
            if constructed_url not in constructed_urls:
                constructed_urls.append(constructed_url)
                titles.append(title)
    directories_dict = dict(zip(titles, constructed_urls))
    return directories_dict

def get_scholarships(soup, *args):
    df = pd.read_html(str(soup))
    df = df[0]
    print(df)
    return data_clean(df)

def data_clean(df):
    '''need to use iloc instead to target columns'''
    #remove , and $ in column
    #df = df[df['Amount'] != "Varies"]
    #df['amount_cleaned'] = df['Amount'].str.replace(',','')
    #df['amount_cleaned'] = df['amount_cleaned'].str.replace('$', '')
    #df['amount_cleaned'] = df['amount_cleaned'].str.replace('$', '')
    ##df['amount_cleaned'] = pd.to_numeric(df['amount_cleaned']) ## different way to convert str -> int
    #df['amount_cleaned'] = df['amount_cleaned'].astype(int)
    return df

def analysis(df):
    pass
def run():
    pass
