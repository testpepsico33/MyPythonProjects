import inspect
import logging
class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3] #test case name called when we are using inheritance
        #logger = logging.getLogger(__name__)  # "__name__" will give you test case names
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfil.log')
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s :%(message)s ")  # defining log formate how the log should print in output
        fileHandler.setFormatter(
            formatter)  # to give the knowledge of formatter method created formatter object and send it to filehandler
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger