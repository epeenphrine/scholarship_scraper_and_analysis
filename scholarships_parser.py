import pandas as pd
import re

base_url = "https://scholarships.com"
def get_directories(soup):
    directories = []
    for a in soup.findAll('a', href=True):
        text = a.get_text(strip=True)
        href = a['href']
        if re.match(r"^/financial-aid/college-scholarships/scholarship-directory/", href):
            
            compiled = f"{base_url}{href}"
            directories.append(compiled)
    return directories

def get_scholarships(soup):
    df = pd.read_html(str(soup))
    df = df[0]
    print(df)
    
    return df

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