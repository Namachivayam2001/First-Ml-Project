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
                'Ada Boost': AdaBoostRegressor(),
                'Gradient Boost': GradientBoostingRegressor(),
                'Random Forest': RandomForestRegressor(),
                'KNeighbors': KNeighborsRegressor(),
                'Cat Boost': CatBoostRegressor(),
                'xgboost': XGBRegressor()
            }

            model_params = {
                "Linear Regression":{},
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Ada Boost":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boost":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                'KNeighbors': {
                    'n_neighbors': [3, 5, 7, 9],  # Number of neighbors to use
                    'weights': ['uniform', 'distance'],  # Weight function used in prediction
                    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],  # Algorithm used to compute the nearest neighbors
                    #'leaf_size': [30, 40, 50],  # Leaf size passed to BallTree or KDTree
                    #'p': [1, 2],  # Power parameter for the Minkowski metric
                },
                "Cat Boost":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "xgboost":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },                
            }


            logging.info('select best model ..........')

            # get models evaluation report
            model_report:dict = evaluate_model(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test, models=models, params = model_params)
            
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