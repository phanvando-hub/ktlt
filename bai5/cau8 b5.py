print("Ho va ten: Phan Văn Đô")
print("MSSV: 205752020710012")
print("######")
import numpy
import numpy as np
data_type= [('name', '515'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
#create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print (students)
print("Sort by height")
print(np.sort (students, order = 'height'))
