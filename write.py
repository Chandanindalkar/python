# 'a' - Appends to existing file
# 'w' - Overwrites the existing file
# 'w' - w used with a new filename creates a new file
emp_file = open('employee.txt', 'a')
emp_file.write('\nBhoomika - college')
emp_file.close()
