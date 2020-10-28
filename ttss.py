from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def tts_scale(x, y, scaler, encoding=None, test_size=None, random_state=None):
    '''
    Helper function to correctly train-test-split, scale numerical columns, and one-hot-encode categorical features.
    Will return x_train, x_test, y_train, y_test.
    
    Parameters:
    x         ==> input variables from dataframe.
    y         ==> target variable from dataframe.
    encoding  ==> iterable of columns from dataframe to be one-hot-encoded.
    ts        ==> test size from train-test-split.
    rs        ==> random_state for train_test_split function.
    scaler    ==> scaling object used to scale numeric data for x_train and x_test.
    
    '''
    
    if(type(x) != type(pd.DataFrame()) and type(x) != type(pd.Series())):
        raise TypeError('X must be a Pandas DataFrame or Pandas Series.')

    if(type(y) != type(pd.DataFrame()) and type(y) != type(pd.Series())):
        raise TypeError('X must be a Pandas DataFrame or Pandas Series.')
    

    num_cols = x.corr().columns
    cat_cols = []
    
    for col in x.columns:
        if col not in num_cols:
            cat_cols.append(col)
    

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)
    

    
    try:
        x_train_s = pd.DataFrame(scaler.fit_transform(x_train[num_cols]), columns=num_cols)
        x_test_s = pd.DataFrame(scaler.fit_transform(x_test[num_cols]), columns=num_cols)

        x_train_s = x_train_s.set_index(x_train.index)
        x_test_s = x_test_s.set_index(x_test.index)
    except AttributeError:
        raise TypeError('The type of this scaler is not allowed.')

    if encoding is not None:
        
        x_train_cat = pd.get_dummies(x_train[cat_cols],columns=encoding)
        x_test_cat = pd.get_dummies(x_test[cat_cols],columns=encoding)
        x_train_final = pd.merge(x_train_s, x_train_cat, left_index=True, right_index=True)
        x_test_final = pd.merge(x_test_s, x_test_cat, left_index=True, right_index=True)
        
        return x_train_final, x_test_final, y_train, y_test

    else:

        return x_train_s, x_test_s, y_train, y_test
    

    