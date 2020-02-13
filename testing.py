soup = [1,2,3,4,5]
stuff = [{'hello':'world'},
          {'bye': 'bye'}]

for item in stuff:
    print(item)
def optional(soup, *args):
    if args:
        dict_list = args[0]
    if not args:
        dict_list = []

    print(soup)
    print(dict_list)
optional(soup)
print(stuff_list)