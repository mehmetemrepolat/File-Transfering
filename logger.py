import coloredlogs
import logging

coloredlogs.install(level='DEBUG')

deneme = "deneme"

logging.info(deneme)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
