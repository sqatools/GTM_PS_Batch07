import json


def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data

json_data = read_json_data("passenger_data.json")

n = len(json_data)
print(n)
for i in range(n):
    print(json_data[i])
    print(i)

