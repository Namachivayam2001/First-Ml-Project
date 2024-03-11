# House price prediction 
This project is one of the `kaggle` competetion

The data was post by `Anna Jo Morelia`, her Linkedin profile - https://www.linkedin.com/in/annavmontoya/

She took the data from `DataCanary 2016-house price prediction`. DataCanary.ai is an enterprise application that offers autonomous data monitoring for business and IT teams.

### Data discription 
* numbert of rows in dataset:  1460
* numbert of columns in dataset:  81
* That fields are 'Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street','Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig','LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType','HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd','RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType','MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual','BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1','BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating','HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF','LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath','HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual','TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType','GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual','GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF','EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC','Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType','SaleCondition', 'SalePrice'
* Representing missing values in the fields
![alt text](image.png)

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