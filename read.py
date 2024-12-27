from pathlib import Path

file_path = Path(r"C:\Users\Chandan Indalkar\Desktop\New Text Document.txt")
emp_file = open(file_path)
print(emp_file.readline())
emp_file.close()
