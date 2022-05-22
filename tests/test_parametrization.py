import pytest
import os,json
from support.utils import load_data

def pytest_generate_tests(metafunc):
    if "testdata_case1" in metafunc.fixturenames:
        test_data_dir_path = os.path.dirname(os.path.realpath(__file__)).replace('tests','testdata/')
        data = json.load(open(test_data_dir_path + 'openapp.json'))   
        result = data['testcase1']
        metafunc.parametrize("testdata_case1", result)

class Test_parametrize:
        
        # def test_case1(self, testdata_case1):
        #         print('Parameter 1 is ', testdata_case1['parameter1'])
        #         print('Parameter 2 is ', testdata_case1['parameter2'])
        #         print('Parameter 3 is ', testdata_case1['parameter3'])

        @pytest.mark.parametrize(*load_data('openapp.csv','testcase1'))
        def test_pytest(self, parameter1, parameter2, parameter3):
                print('Parameter 1 is ', parameter1)
                print('Parameter 2 is ', parameter2)
                print('Parameter 3 is ', parameter3)