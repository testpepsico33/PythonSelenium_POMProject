from configparser import ConfigParser


def read_configuration(category,key):
    config =ConfigParser()
    config.read("C:\Users\nimalkumar.j\PycharmProjects\HybridePythonSeleniumFramework\configurations\config.ini")
    return config.get(category,key)
