import scholarships_parser
import connection
from config import url


soup = connection.connect()
scholarships_parser.get_directories(soup)