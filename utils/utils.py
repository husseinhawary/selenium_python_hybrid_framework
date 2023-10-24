import json
from configparser import ConfigParser
from datetime import datetime


class Utils:

    @staticmethod
    def generate_email_with_current_time_stamp():
        current_datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "hussein" + current_datetime + "@gmail.com"

    @staticmethod
    def json_data_reader(file_path):
        with open(file_path) as file_object:
            data = json.load(file_object)
            return data

    @staticmethod
    def read_configurations(category, key):
        configs = ConfigParser()
        configs.read("configurations/config.ini")
        return configs.get(category, key)
