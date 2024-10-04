import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    return_tuple = data_split(*feature_target_sample)
    # TODO test if the length of return_tuple is 4
    # Unpack the return from data_split
    train_features, test_features, train_target, test_target = data_split(*feature_target_sample)

    # Test if the length of return_tuple is 4 (train_features, test_features, train_target, test_target)
    assert len((train_features, test_features, train_target, test_target)) == 4

    # Assert that the lengths of the train and test sets are expected, given the test_size (assumed)
    assert len(train_features) == len(train_target)
    assert len(test_features) == len(test_target)

    # Check if the split was deterministic if random_state is set
    assert train_features.shape[0] + test_features.shape[0] == feature_target_sample[0].shape[0]
    assert train_target.shape[0] + test_target.shape[0] == feature_target_sample[1].shape[0]
    #raise NotImplemented
