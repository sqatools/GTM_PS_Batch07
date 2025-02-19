import json
import os
from datetime import datetime

class Utils:
    def read_json_file(self, file_name):
        with open(file_name) as file:
            data = file.read()
            return json.loads(data)

    def get_time_stamp_name(self):
        return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        #return datetime.now()


    def get_image_file_path(self):
        cur_wd = os.getcwd()
        image_path = os.path.join(cur_wd, "logs\images")
        if not os.path.exists(image_path):
            os.mkdir(image_path)
        return image_path





if __name__ == '__main__':
    obj = Utils()
    # data = obj.read_json_file("test_data.json")
    # print(data['depart_date'])
    print(obj.time_stamp_name())
