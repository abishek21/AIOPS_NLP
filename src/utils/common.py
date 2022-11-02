import os
import yaml
import logging
import time
import pandas as pd
import json
import gdown

def download_data(url_link,out_path):
    url = url_link
    output = out_path
    gdown.download(url, output, quiet=False)
    logging.info("data downloaded successfully")


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    if type(path_to_directories)!=list:
        raise TypeError("path_to_directories must be a list")
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")

def get_df(path_to_data:str,sep:str='\t') -> pd.DataFrame:
    df=pd.read_csv(path_to_data,
                   encoding='utf-8',
                   header=None,
                   delimiter=sep,
                   names=['id','label','text']
                   )
    logging.info(f'The input data frame {path_to_data}  size is {df.shape}\n')
    return df