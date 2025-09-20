# this file will contain everything related to transformation of data
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    # TEMPORARY DEBUGGING BLOCK
    def test_pipelines(self):
        try:
            logging.info("--- STARTING PIPELINE DEBUG ---")
            
            # Create small dummy data to test
            test_data = {
                'gender': ['male', 'female'],
                'race_ethnicity': ['group A', 'group B'],
                'parental_level_of_education': ["bachelor's degree", 'some college'],
                'lunch': ['standard', 'free/reduced'],
                'test_preparation_course': ['none', 'completed'],
                'reading_score': [72, 69],
                'writing_score': [74, 90]
            }
            df = pd.DataFrame(test_data)
            
            logging.info("Dummy DataFrame created.")
            
            preprocessor_obj = self.get_data_transformer_object()
            
            logging.info("Preprocessor object created. Now transforming...")
            
            # This is the line that fails. Let's see what happens.
            transformed_data = preprocessor_obj.fit_transform(df)
            
            logging.info("--- PIPELINE DEBUG SUCCEEDED ---")
            logging.info(f"Output shape: {transformed_data.shape}")
            logging.info(f"Output type: {type(transformed_data)}")

        except Exception as e:
            logging.error("--- PIPELINE DEBUG FAILED ---")
            import traceback
            logging.error(traceback.format_exc())
            raise CustomException(e, sys)
        
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # Pipeline for numerical features
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    # This line MUST have with_mean=False
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            # Pipeline for categorical features
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore'))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipelines", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)



    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("read train and test data")
            logging.info("obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_object()

            
            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            logging.info("applied preprocessing")
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr= np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr= np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            logging.info("saving preprocessing objects")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

   
            
        
        