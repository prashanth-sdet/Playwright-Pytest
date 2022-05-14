import yaml, csv, json
from yaml.loader import SafeLoader
import os 


def load_data(filename,testcase='default'):
    test_data_dir_path = os.path.dirname(os.path.realpath(__file__)).replace('support','testdata/')

    stringified_params = ''
    list_result = []

    if filename.endswith('.yml'):
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

        for index in range(max_length):
            temp_list = list()
            for key in data[testcase]:
                temp_list.append(data[testcase][key][index])
            list_result.append(tuple(temp_list))

    elif filename.endswith('.csv'):
        with open(test_data_dir_path + filename, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')

            for index,row in enumerate(data):
                temp_list = list()            
                if index==0:
                    stringified_params = ','.join(row)  
                else:
                    for value in row:
                        temp_list.append(value)
                    list_result.append(tuple(temp_list))

    elif filename.endswith('.json'):
        data = json.load(open(test_data_dir_path + filename))   
        stringified_params = ','.join(data[testcase][0])

        for item in data[testcase]:
            temp_list = list()
            for key in item:
                temp_list.append(item[key])
            list_result.append(temp_list)
        
    return stringified_params, list_result
