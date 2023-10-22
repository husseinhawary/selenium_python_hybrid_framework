from configparser import ConfigParser


def read_configurations(category, key):
    configs = ConfigParser()
    configs.read("configurations/config.ini")
    return configs.get(category, key)
