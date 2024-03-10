import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
FILE_PATH = os.path.join(os.getcwd(), 'logs', LOG_FILE)

os.makedirs(os.path.join(os.getcwd(), 'logs'), exist_ok=True)

logging.basicConfig(
    filename = FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
