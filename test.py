import scholarships_parser
from connection import connect 
from config import url
from proxyscrape import proxyscrape as scrape


soup = connect(url)
scholarships_parser.get_directories(soup)

#scholarships_parser.get_directories(soup)