import json

path_values = input("Enter the default path of the Values file: ")
path_tests = input("Enter the default path of the Tests file: ")
path_report = input("Enter the path where you want to save the Report file: ")

with open(path_tests, encoding="UTF-8") as file_tests:
    records_tests = json.load(file_tests)
    file_tests.close()

with open(path_values, encoding="UTF-8") as file_values:
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
with open(path_report, "w") as file_report:
    json.dump(report, file_report)
