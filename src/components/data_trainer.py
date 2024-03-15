import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_model
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.neighbors import KNeighborsRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('model trainer initiated ..........')

            x_train, x_test, y_train, y_test = (
                train_array[:, :-1],
                test_array[:, :-1],
                train_array[:, -1],
                test_array[:, -1]
            )

            models = {
                'Linear Regression': LinearRegression(),
                'Decision Tree': DecisionTreeRegressor(),
                'SVM': SVR(),
                'Ada Boost': AdaBoostRegressor(),
                'Gradient Boost': GradientBoostingRegressor(),
                'Random Forest': RandomForestRegressor(),
                'KNeighbors': KNeighborsRegressor(),
                'Cat Boost': CatBoostRegressor(),
                'xgboost': XGBRegressor()
            }

            logging.info('select best model ..........')

            # get models evaluation report
            model_report:dict = evaluate_model(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test, models=models)
            
            report_df = pd.DataFrame(model_report, index=None)
            best_model_record = report_df[report_df['test accuracy'] == report_df['test accuracy'].max()]
            best_model_score = best_model_record['test accuracy'].iloc[0]
            best_model_name = best_model_record['model'].iloc[0]
            best_model = models[best_model_name]


            if(best_model_score < 0.6):
                raise CustomException('Best model not found')
            
            logging.info('save the model ..........')
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                object=best_model
            )

            logging.info('model trainer closed ..........')

            return self.model_trainer_config.trained_model_file_path

        except Exception as e:
            raise CustomException(e, sys)