import pandas as pd
import sklearn
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import joblib

model_filename = './model.pkl'
imputer_filename = './imputer.pkl'
scaler_filename = './scaler.pkl'

def preprocess_data(data, imputer=None, scaler=None):
    
# -------------------------- 请调整你的数据预处理过程 ---------------------------
## 输入：
#### data 为 pandas.DataFrame类型数据
#### imputer 为缺失值填充方式
#### scaler 为数据归一化方式
## 输出：
#### data_norm 为处理后的数据，为 pandas.DataFrame类型数据
   
    column_name = ['Year', 'Life expectancy ', 'infant deaths', 'Alcohol',
               'percentage expenditure', 'Hepatitis B', 'Measles ', ' BMI ', 'under-five deaths ',
               'Polio', 'Total expenditure', 'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
               ' thinness  1-19 years', ' thinness 5-9 years', 'Income composition of resources',
               'Schooling']
    data = data.drop(["Country", "Status"], axis=1)
    
    if imputer==None:
        imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
        imputer = imputer.fit(data[column_name])
    data[column_name] = imputer.transform(data[column_name])
    
    if scaler==None:
        scaler = MinMaxScaler()
        scaler = scaler.fit(data)
    data_norm = pd.DataFrame(scaler.transform(data), columns=data.columns)
    
    data_norm = data_norm.drop(['Year'], axis = 1)
    
    return data_norm

def predict(test_data):
    
# -------------------------- 请加载您最满意的模型 ---------------------------
# 加载模型(请加载你认为的最佳模型)
# 加载模型,加载请注意 filename 是相对路径, 与当前文件同级。 
# test_data 为 pandas.DataFrame类型数据
    loaded_model = joblib.load(model_filename)
    imputer = joblib.load(imputer_filename)
    scaler = joblib.load(scaler_filename)
    
    test_data_norm = preprocess_data(test_data, imputer, scaler)
    test_x = test_data_norm.values
    predictions = loaded_model.predict(test_x)
    
    return predictions
