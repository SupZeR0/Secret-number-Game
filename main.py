import csv

def read_csv_file(file_name):
  with open(file_name) as f:
    csv_data =csv.reader(f)
    data_lst = list(csv_data)
  return data_lst
  
def double_salary(emps_lst):
  for employee in emps_lst:
    salary = employee[-1].replace(',', '').replace('"', '')
    employee[-1] = str(float(salary) * 2)
  return emps_lst

emps_lst = read_csv_file('employees_data.csv')
update_salary = double_salary(emps_lst)

def get_salary(employee):
  return float(employee[-1])
  
sorted_emps_data = sorted(update_salary,key=get_salary)

print(sorted_emps_data)