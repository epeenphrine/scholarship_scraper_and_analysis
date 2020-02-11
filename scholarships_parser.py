import pandas as pd


def get_directories(soup):
    directories = []
    for a in soup.findAll('a', href=True):
        text = a.get_text(strip=True)
        href = a['href']
        if "financial-aid" in href:
            print(f"text {text}\n")
            print(href)
    return directories

def get_scholarships(soup):
    df = pd.read_html(str(soup))
    print(df)