import json
import sys
import argparse


def create_path_numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_values', nargs='?')
    parser.add_argument('path_tests', nargs='?')
    parser.add_argument('path_report', nargs='?')

    return parser


if __name__ == '__main__':
    parser = create_path_numbers()
    data = parser.parse_args()

    with open(data.path_tests, encoding="UTF-8") as file_tests:
        records_tests = json.load(file_tests)
        file_tests.close()

    with open(data.path_values, encoding="UTF-8") as file_values:
        records_values = json.load(file_values)
        file_values.close()

    test = records_tests['tests']
    values = records_values['values']


    def checking_and_overwriting_value(record_tests_value):
        for record_values in values:
            if 'value' in record_tests_value.keys() and record_tests_value['value'] == '':
                if record_values['id'] == record_tests_value['id']:
                    record_tests_value['value'] = record_values['value']


    def view_next(current_depth, record_tests_next):
        for i in range(len(current_depth)):
            for k1, v1 in current_depth[i].items():
                if type(v1) == list:
                    if type(current_depth[i]) == list:
                        view_next(v1, current_depth[i])
                    else:
                        view_next(v1, current_depth[i][k1])
            if type(current_depth[i]) != list:
                checking_and_overwriting_value(current_depth[i])
            else:
                checking_and_overwriting_value(record_tests_next)


    for record_tests in test:
        for k, v in record_tests.items():
            if type(v) == list:
                view_next(v, record_tests[k][0])
            checking_and_overwriting_value(record_tests)

    report = {'reports': test}
    with open(data.path_report, "w") as file_report:
        json.dump(report, file_report)
