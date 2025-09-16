import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_Path=os.path.join(logs_path,LOG_FILE)

print("Working directory:", os.getcwd())
print("Log file will be at:", LOG_FILE_Path)

logging.basicConfig(
    filename=LOG_FILE_Path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,

)
if __name__=="__main__":
    logging.info("logging has started")
    logging.warning("WARNING TEST ENTRY")
    if os.path.exists(LOG_FILE_Path):
        print("Log file created successfully!")
    else:
        print("Log file NOT created.")