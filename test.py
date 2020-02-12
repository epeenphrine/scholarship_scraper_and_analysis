import scholarships_parser
from connection import connect 
from config import url
from proxyscrape import proxyscrape as scrape


soup = connect(url)
print(soup)

#scholarships_parser.get_directories(soup)