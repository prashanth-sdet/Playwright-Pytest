import yaml, csv, json
from yaml.loader import SafeLoader
import os 


def load_data(filename,testcase='default'):
    test_data_dir_path = os.path.dirname(os.path.realpath(__file__)).replace('support','testdata/')

    stringified_params = ''
    list_result = []

    if filename.endswith('.json'):
        data = json.load(open(test_data_dir_path + filename))   
        stringified_params = ','.join(data[testcase][0])
        list_result = [[item[key] for key in item] for item in data[testcase]]

    elif filename.endswith('.yml'):
        with open(test_data_dir_path + filename) as f:
            data = yaml.load(f, Loader=SafeLoader)

        stringified_params = ','.join(data[testcase].keys())
        max_length = 1

        for key in data[testcase]:
            if len(data[testcase][key]) > max_length:
                max_length = len(data[testcase][key])
        
        for key in data[testcase]:
            if len(data[testcase][key]) < max_length:
                data[testcase][key].append(data[testcase][key][0])

        list_result = [[data[testcase][key][index] for key in data[testcase]] for index in range(max_length)]

    elif filename.endswith('.csv'):
        with open(test_data_dir_path + filename, newline='') as csvfile:
            data = list(csv.reader(csvfile, delimiter=','))
            stringified_params = ','.join(data[0])
            list_result = data[1:]
            
    return stringified_params, list_result
