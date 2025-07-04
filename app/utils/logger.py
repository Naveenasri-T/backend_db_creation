
import logging

logger = logging.getLogger("student_logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/app.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
