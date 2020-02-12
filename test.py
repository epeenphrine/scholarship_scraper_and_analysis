import scholarships_parser
from connection import connect
from config import url


soup = connect(url)
soup_pool = []
soup_puddle = []
directories_list1 = scholarships_parser.get_directories(soup)

for url in directories_list1:
    soup_pool.append(connect(url))
for soup1 in soup_pool:
    soup_puddle.append(scholarships_parser.get_directories(soup1))

checking = []
for items in soup_puddle:
    for item in items:
        if item not in checking:
            checking.append(item)

for item in checking:
    print (item)

print(len(checking))
#scholarships_parser.get_scholarships(soup)