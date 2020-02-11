import scholarships_parser
import connection
from config import url


soup = connection.connect(url)
#scholarships_parser.get_directories(soup)
scholarships_parser.get_scholarships(soup)