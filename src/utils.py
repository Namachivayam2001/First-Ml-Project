import os
import sys
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, object):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as fp:
            dill.dump(object, fp)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(x_train, x_test, y_train, y_test, models, params):
    try:
        report = {
            'model': [],
            'train accuracy': [],
            'test accuracy': []
        }
        
        for i in range(len(list(models))):
            # initiate mode
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(x_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train, y_train)

            # make prediction
            y_train_prd = model.predict(x_train)
            y_test_prd = model.predict(x_test)

            # find r2 score
            train_r2_score = r2_score(y_train, y_train_prd)
            test_r2_score = r2_score(y_test, y_test_prd)

            # append the scores in report
            report['model'].append(list(models.keys())[i])
            report['train accuracy'].append(train_r2_score)
            report['test accuracy'].append(test_r2_score)

        return report 
    
    except Exception as e:
        raise CustomException(e, sys)