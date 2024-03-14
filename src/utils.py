import pandas as pd
import numpy as np
import os
import sys
import dill
from src.exception import CustomException

def save_object(file_path, object):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as fp:
            dill.dump(object, fp)

    except Exception as e:
        raise CustomException(e, sys)