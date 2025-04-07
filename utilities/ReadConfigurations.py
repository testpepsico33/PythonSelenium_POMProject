from configparser import ConfigParser
import configurations
def readConfigurations(category,key):
    config = ConfigParser()
    config.read("C://Users//nimalkumar.j//PycharmProjects//HybridePythonSeleniumFramework//configurations//config.ini")
    #In confttest file browse and url is hardoaded
    return config.get(category,key)