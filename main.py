import csv
def main():
  # read the data
  employees_lst = read_csv_file('employees_data.csv')

  # update the salary
  updated_employees_data = update_salary(employees_lst) 

  #sort the data 
  sorted_employees_data =sort_data(updated_employees_data)

  # write the data to the new file 
  write_csv_file('new_employees',sorted_employees_data)
  
  print("done")

def read_csv_file(file_name):
  """Get file name
    Read the data from the file 
    Return the data in the file as a list"""
  with open(file_name) as f:
    csv_data = csv.reader(f)
    data_lst = list(csv_data)
  return data_lst

def update_salary(employees_lst):
  """Get the employees list
    Update salary
    Return list after updating salary"""
  for employee in employees_lst:
    salary = employee[-1].replace(',', '').replace('"', '')
    employee[-1] = str(float(salary) * 2)
  return employees_lst

def sort_data(updated_employees_data):
  sorted_employees_data = sorted(updated_employees_data,key=lambda employee:(employee[-1],employee[0]))
  return sorted_employees_data

def write_csv_file(file_name, new_data):
  """Get file name and data to be written
  Write data as a CSV file"""
  with open(file_name,'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(new_data)


if __name__ == '__main__':
  main()