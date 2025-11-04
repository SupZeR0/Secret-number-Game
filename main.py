import csv

def read_csv_file(file_name):
  with open(file_name) as f:
    csv_data =csv.reader(f)
    data_lst = list(csv_data)
  return data_lst

emps_lst = read_csv_file('employees_data.csv')


for employee in emps_lst: 
  emp_data = employee[0].split(' - ')
  emp_data[-1] = str(float(emp_data[-1]) * 2)
  print(' - '.join(emp_data))