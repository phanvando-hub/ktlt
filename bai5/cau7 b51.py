import numpy as np
data_type [('name', '515'), ('class', int), ('height', float)1 = students details = [('Minh', 5, 48.5), ('Hoang', 5, 40,56), ('Son', 5,
42.10), ('Phong', 5, 40.11)]
#create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print (students)
print("Sort by height")
print (np.sort (students, order 'height'))
