import json

def read_json_file(filepath):
    with open(filepath,"r") as file:
        content = file.read()
        json_data = json.loads(content)
        print(json_data)

read_json_file("test_data.json")