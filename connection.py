import os
import json
import time
import random
import urllib.request
import bs4 as bs
import proxyscrape as scrape
from config import url


#file checks / proxy rotation / connection 
def connect(url):
    if os.path.exists("proxydictlist.json"):
        with open("proxydictlist.json") as f:
            proxies_list = json.load(f)
            print(f"attempting to connect to: {url}")
            print(len(proxies_list))
    else:
        print("proxydictlist.json doesn't exist creating new proxylist")
        time.sleep(2)
        scrape.proxyscrape()
        with open("proxydictlist.json") as f:
            proxies_list = json.load(f)
            print(f"attempting to connect to: {url}")
            print(len(proxies_list))

    if len(proxies_list) >= 100:
        for i in range(0, len(proxies_list)):
            try:
                pick = random.choice(proxies_list)

                ## building opener
                proxy_support = urllib.request.ProxyHandler(pick)
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)

                ## requests
                req = urllib.request.Request(url, headers={'User-Agent': "Mozilla/5.0"})
                sauce = urllib.request.urlopen(req, timeout=1).read()
                soup = bs.BeautifulSoup(sauce, 'lxml')


                print(f"{pick} WORKED")
                ## break off the loop when we have a working proxy
                return soup
            except:
                print(f"{pick} did not work")
                proxies_list.remove(pick)
                print(f"{pick} removed")
                print(len(proxies_list))

            with open("proxydictlist.json", "w") as f:
                json.dump(proxies_list, f)
            print("\n\n\n\n\n\n\n\n")
    else:
        print("\n\n")
        print("getting new proxies")
        scrape.proxyscrape()
        print("\n")
        print("got new proxies ..... ")
        return connect(url)