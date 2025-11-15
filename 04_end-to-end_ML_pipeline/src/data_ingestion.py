import pandas as pd
import os 
from sklearn.model_selection import train_test_split
import logging 
import yaml

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("data_ingestion")
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, "data_ingestion.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



def load_params(params_path):

    try:
        with open(params_path, "r") as file:
            params = yaml.safe_load(file)
        logger.debug("Params Retreived from %s", params_path)
        return params
    except FileNotFoundError:
        logger.error("Params file not found at %s", params_path)
        raise
    except yaml.YAMLError as e:
        logger.error("Error loading params from %s: %s", e)
        raise
    except Exception as e:
        logger.error("Error loading params from %s: %s", e)
        raise


def load_data(data_url):

    try:
        df = pd.read_csv(data_url)
        logger.debug("Data Loaded from %s", data_url)
        return df
    except pd.errors.ParserError as e:
        logger.error("Error loading data from %s: %s", e)
        raise
    except Exception as e:
        logger.error("Error loading data from %s: %s", e)
        raise


def preprocess_data(df):

    try:
        df.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)
        df.rename(columns = {'v1': 'target', 'v2': 'text'}, inplace=True)
        logger.debug("Data Preprocessed Completed")
        return df
    except KeyError as e:
        logger.error("Missing columns in data: %s", e)
        raise
    except Exception as e:
        logger.error("Error preprocessing data: %s", e)
        raise
        

def save_data(train_data, test_data, data_path):

    try:
        raw_data_path = os.path.join(data_path, "raw_data")
        os.makedirs(raw_data_path, exist_ok=True)
        train_data.to_csv(os.path.join(raw_data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(raw_data_path, "test.csv"), index=False)
        logger.debug("Train and Test data saved to %s", raw_data_path)
    except Exception as e:
        logger.error("Error saving data: %s", e)
        raise



def main():

    try:
        params = load_params("D:/MLOps/04_end-to-end_ML_pipeline/params.yaml")
        test_size = params['data_ingestion']['test_size']

        data_path = 'https://raw.githubusercontent.com/vikashishere/Datasets/main/spam.csv'
        df = load_data(data_path)
        final_df = preprocess_data(df)
        
        train_df, test_df = train_test_split(final_df, test_size=test_size, random_state=42)
        
        save_data(train_df, test_df, data_path='D:/MLOps/04_end-to-end_ML_pipeline/data')
    except Exception as e:
        logger.Error("Failed to run data ingestion pipeline: %s", e)
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
        