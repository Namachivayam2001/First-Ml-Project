import sys
from src.logger import logging
from src.exception import CustomException
import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngesionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')

class DataIngesion:
    def __init__(self):
        self.data_path = DataIngesionConfig()

    def initiate_data_ingesion(self):
        logging.info('initiate data ingesion ..........')
        try:

            logging.info('data read initiated ..........')
            df = pd.read_csv('notebook/data/train.csv')
            logging.info('data read completed ..........')

            logging.info('train test split initiated ..........')
            train, test = train_test_split(df, test_size=0.2, random_state=42)
            logging.info('train test split completed ..........')

            logging.info('save train test split initiated ..........')
            os.makedirs(os.path.dirname(self.data_path.raw_data_path), exist_ok=True)
            df.to_csv(self.data_path.raw_data_path, header=True, index=True)
            train.to_csv(self.data_path.train_data_path, header=True, index=True)
            test.to_csv(self.data_path.test_data_path, header=True, index=True)
            logging.info('save train test split completed ..........')

        except Exception as e:
            raise CustomException(e, sys)
        