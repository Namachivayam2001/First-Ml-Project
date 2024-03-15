import pandas as pd
import numpy as np
import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object
from dataclasses import dataclass

from src.components.data_ingesion import DataIngesion
from src.components.data_trainer import ModelTrainer

from scipy.sparse import hstack

@dataclass
class DataTransformerConfig:
    preprocesor_obj_file_path = os.path.join('artifacts', 'preprocesor.pkl')

class DataTransformer:
    def __init__(self):
        self.data_transformer_config = DataTransformerConfig()
    
    def get_data_transformer(self):
        try:
            num_columns = [
                'MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond',
                'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
                'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
                'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
                'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
                'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
                'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
                'MoSold', 'YrSold'
            ]
            cat_columns = [
                'MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities',
                'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
                'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
                'Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
                'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating',
                'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional',
                'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive',
                'SaleType', 'SaleCondition'
            ]

            logging.info('start catagorical pipeline ..........')
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('encoder', OneHotEncoder(handle_unknown='ignore')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info('end catagorical pipeline ..........')

            logging.info('start numarical pipeline ..........')
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='mean')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info('end numarical pipeline ..........')

            preprocessing = ColumnTransformer([
                ('cat_pipeline_transformer', cat_pipeline, cat_columns),
                ('num_pipeline_transformer', num_pipeline, num_columns)
            ])
            return preprocessing
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformer(self, train_path, test_path):
        try:
            logging.info('data transformer initiated ..........')
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('preprocessor object initiated ..........')
            preprocessing_obj = self.get_data_transformer()

            target_column = 'SalePrice'
            feature_train_df = train_df.drop(columns=[target_column], axis=1)
            target_train_df = train_df[target_column]
            feature_test_df = test_df.drop(columns=[target_column], axis=1)
            target_test_df = test_df[target_column]

            logging.info('transform the features using preprocessor object ...........')
            input_feature_train_arr = preprocessing_obj.fit_transform(feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(feature_test_df)

            logging.info('concatinate the input features array amd target as array ..........')
            train_arr = hstack((input_feature_train_arr, np.array(target_train_df)[:, np.newaxis]))
            test_arr = hstack((input_feature_test_arr, np.array(target_test_df)[:, np.newaxis]))

            logging.info('save preprocessing object ..........')
            save_object(
                file_path = self.data_transformer_config.preprocesor_obj_file_path,
                object = preprocessing_obj
            )

            return (
                train_arr.toarray(),
                test_arr.toarray()
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    obj = DataIngesion()
    train_data_path, test_data_path = obj.initiate_data_ingesion()

    transformer_obj = DataTransformer()
    train_arr, test_arr = transformer_obj.initiate_data_transformer(train_data_path, test_data_path)

    trainer_obj = ModelTrainer()
    trained_model_path = trainer_obj.initiate_model_trainer(train_arr, test_arr)

