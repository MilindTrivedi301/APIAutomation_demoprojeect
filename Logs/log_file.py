import logging

def log_fuc():
    logger = logging.getLogger()
    filehandler = logging.FileHandler("logfile.log")
    #filehandler = logging.FileHandler("..\\pythonProject\\Logs\\current_log_file.log")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger