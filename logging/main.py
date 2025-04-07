import logging

def log_details():
    logging.basicConfig(filename="demo.log", #seperate log file will be created to store logs
                        level=logging.INFO,
                        format='%(asctime)s -%(levelname)s -%(message)s',
                        datefmt='%Y-%m-%d%H:%M:%S %p')
    return logging.getLogger()
#wherever logger.info is called ,
logger=log_details()
logger.info("Program execution started") #info related to getLogger

a=4
b=3

if a<b:
    print("Nirmal")
    logger.info("a is greater than b, hence arun got printed in output")

logger.info("Program Execution ended")
