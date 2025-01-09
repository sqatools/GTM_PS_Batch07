import json

def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        print(json_data)
        return json_data

json_data = read_json_data("test_json_file.json")
print("Name:", json_data['Name'])
print("Email:", json_data['Email'])
print("Phone:", json_data['Phone'])
