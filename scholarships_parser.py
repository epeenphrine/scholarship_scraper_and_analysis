
def get_directories(soup):
    search = soup.findAll('a', href=True)
    directories = []
    for a in search:
        if a.text:
            directories.append(a['href'])
    print(directories)
    return directories
