# House price prediction 
This project is one of the `kaggle` competetion

The data was post by `Anna Jo Morelia`, her Linkedin profile - https://www.linkedin.com/in/annavmontoya/

She took the data from `DataCanary 2016-house price prediction`. DataCanary.ai is an enterprise application that offers autonomous data monitoring for business and IT teams.

In the `kaggle` competesion they denote that we use `RMSE` for model evaluation

### Data discription 
* numbert of rows in dataset:  1460
* numbert of columns in dataset:  81
* Deficult to describe the all features. So I put the seperate text file for data discription named 'data_description.txt' 
* That fields are 'Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street','Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig','LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType','HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd','RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType','MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual','BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1','BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating','HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF','LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath','HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual','TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType','GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual','GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF','EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC','Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType','SaleCondition', 'SalePrice'
* Representing missing values in the fields
|----|----------------|-----------------|-----------------------------|
| 	 |  Fields	      | Missing Counts	|  Missing Count Persentage   |
|----|----------------|-----------------|-----------------------------|
| 0	 |  LotFrontage	  |   259	        |       17.739726             |
| 1	 |  Alley	      |   1369	        |       93.767123             |
| 2	 |  MasVnrType	  |   872	        |       59.726027             |
| 3	 |  MasVnrArea	  |   8	            |       0.547945              |
| 4	 |  BsmtQual	  |   37	        |       2.534247              |
| 5	 |  BsmtCond	  |   37	        |       2.534247              |
| 6	 |  BsmtExposure  |	  38            |       2.602740              |
| 7	 |  BsmtFinType1  |	  37            |       2.534247              |
| 8	 |  BsmtFinType2  |	  38            |       2.602740              |
| 9	 |  Electrical	  |   1	            |       0.068493              |
| 10 |  FireplaceQu	  |   690	        |       47.260274             |
| 11 |  GarageType	  |   81	        |       5.547945              |
| 12 |  GarageYrBlt	  |   81	        |       5.547945              |
| 13 |  GarageFinish  |	  81            |       5.547945              |
| 14 |  GarageQual	  |   81	        |       5.547945              |
| 15 |  GarageCond	  |   81	        |       5.547945              |
| 16 |  PoolQC	      |   1453	        |       99.520548             |
| 17 |  Fence	      |   1179	        |       80.753425             |
| 18 |  MiscFeature	  |   1406	        |       96.301370             |
|----|----------------|-----------------|-----------------------------|

* Drop 'Alley', 'MasVnrType', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature' because of missing values grater then 25%
* Drop 'Id' for feature importance 
* After handling missing values features from the dataframe is 74

### Model 
* I consider 7 regresion models for this project. 
1, Linear Regression
2, K-Neighbors Regressor
3, Decision Tree Regressor
4, Random Forest Regressor
5, XGBRegressor
6, CatBoosting Regressor
7, AdaBoost Regresso

* After train the above all, I got the result
|---|-------------------------|-----------------|---------------|-----------------|-----------------|        
| 	| Model	                  |  Train_RMSE	    | Test_RMSE	    | Train_R2_Square |	 Test_R2_Square |  
|---|-------------------------|-----------------|---------------|-----------------|-----------------|
| 0	| Linear Regression	      |  19938.799110	| 4.567150e+14	| 0.933347	      |  -2.719423e+19  | 
| 1	| K-Neighbors Regressor	  |  31632.579164	| 3.851088e+04	| 0.832239	      |  8.066460e-01   |
| 2	| Decision Tree Regressor |	 0.000000	    | 4.327226e+04	| 1.000000	      |  7.558789e-01   |
| 3	| Random Forest Regressor |	 11466.582413	| 2.959065e+04	| 0.977956	      |  8.858450e-01   |
|`4`|`XGBRegressor`	          | `1183.757328`	|`2.572988e+04` |`0.999765`	      | `9.136899e-01`  |
| 5	| CatBoosting Regressor	  |  5752.350224	| 2.743765e+04	| 0.994452	      |  9.018523e-01   |
| 6	| AdaBoost Regressor	  |  27378.057826	| 3.593371e+04	| 0.874331	      |  8.316588e-01   |
|---|-------------------------|-----------------|---------------|-----------------|-----------------|

* I choose `XGBRegressor`, Because of minimum `RMSE` and high `R2_Score` 