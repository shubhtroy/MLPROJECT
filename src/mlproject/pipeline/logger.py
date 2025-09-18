import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_Path=os.path.join(logs_path,LOG_FILE)

print("Working directory:", os.getcwd())
print("Log file will be at:", LOG_FILE_Path)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_FILE_Path)
file_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)
