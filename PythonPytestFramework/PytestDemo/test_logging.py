import logging

def test_loggingDemo():

  logger =logging.getLogger(__name__) #"__name__" will give you test case names

  fileHandler=logging.FileHandler('logfil.log')
  formatter =logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s ") #defining log formate how the log should print in output
  fileHandler.setFormatter(formatter) #to give the knowledge of formatter method created formatter object and send it to filehandler
  logger.addHandler(fileHandler) #filehandler object -->addHandler will take filehandler object -->fileHandler nothing its a file location
  #logger have knowledge which file to print which is taken from filehandler object

  logger.setLevel(logging.DEBUG) #setting level from where the info should run
  logger.debug("A debug statement is executed") #We can give some idea how can we debug the issue
  logger.info("information statement")
  logger.warning("Something is in warning mode")
  logger.error("A majore error has happened")
  logger.critical("Critical issue")
