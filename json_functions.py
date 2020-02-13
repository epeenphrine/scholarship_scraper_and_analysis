import json

def json_load(file_name):
    with open("proxydictlist.json") as f:
        print("json file exists")
        time.sleep(1)
         json_file = json.load(f)
        return json_file

def json_create(file_name ):
    with open("proxydictlist.json", "w") as f:
        json.dump([], f)
        time.sleep(1)
        return