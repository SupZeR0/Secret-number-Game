import csv

def read_csv_file(file_name):
  with open(file_name) as f:
    csv_data =csv.reader(f)
    data_lst = list(csv_data)
  return data_lst
  
def double_salary(emps_lst):
  updated_list = []
  for employee in emps_lst:
    emp_data = employee[0].split(' - ')
    emp_data[-1] = str(float(emp_data[-1]) * 2)
    updated_list.append(' - '.join(emp_data))
  return updated_list

emps_lst = read_csv_file('employees_data.csv')

update_salary =double_salary(emps_lst)
print(update_salary)