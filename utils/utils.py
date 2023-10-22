import json
from datetime import datetime


def generate_email_with_current_time_stamp():
    current_datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "hussein" + current_datetime + "@gmail.com"


def json_data_reader(file_path):
    with open(file_path) as file_object:
        data = json.load(file_object)
        return data
