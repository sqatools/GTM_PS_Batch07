import json

class Utils:
    def read_json_file(self, file_name):
        with open(file_name) as file:
            data = file.read()
            return json.loads(data)


if __name__ == '__main__':
    obj = Utils()
    data = obj.read_json_file("test_data.json")
    print(data['depart_date'])
