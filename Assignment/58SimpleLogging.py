# 58. Simple Logging
import logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')
logging.info("This is an info message.")
logging.error("This is an error message.")