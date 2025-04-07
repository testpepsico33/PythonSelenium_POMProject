import logging


def generate_logs():
    logging.basicConfig(filename="tutorialNinja.log", #seperate log file will be created to store logs
                        level=logging.INFO,
                        format='%(asctime)s -%(levelname)s -%(message)s',
                        datefmt='%Y-%m-%d%H:%M:%S %p')
    return logging.getLogger()