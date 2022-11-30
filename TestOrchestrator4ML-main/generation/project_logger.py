import logging

def getInfoLogger():
    logging.basicConfig(filename='../PROJECT-GENERATION-LOG.LOG', level=logging.INFO, format='%(asctime)s:::%(name)s:::%(levelname)s:::%(message)s', datefmt='%d-%b-%y %H:%M:%S') 
    loggerObj = logging.getLogger('project-logger') 
    return loggerObj 
