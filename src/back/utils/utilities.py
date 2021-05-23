import pickle
import pandas as pd


def read_data(input_file_name):
    data = pd.read_csv(input_file_name)
    return data['name']

def read_data_pickle(input_file_name):
    data = pickle.load(input_file_name)
    return data

def write_data_to_file(output_file_name, data):
    with open(output_file_name, 'wb') as out_file:
        pickle.dump(data, out_file)
