
# dictionary

student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
print(student)
print(student['name'])
print(student.get('phone','Not Found'))     # get method

# adding value to dictionary

student['phone'] = '5555-5555'    # adding new value in dict
print(student)
student.update({'name':'Jack'})   # update method
print(student)

del student['age']       # del method
print(student)

phone = student.pop('phone')    # pop method
print(phone)

# Dictionary

stud = {'name': 'John', 'age': '20', 'phone': '555'}
print(stud)
print(stud['name'])
print(stud.get('phone'))
print(stud.get('course','Not Found'))
stud.update({'courses':'Math'})
del stud['phone']
print(stud)
age = stud.pop('age')
print(stud)
print(age)

print(stud.values())
print(stud.keys())
print(stud.items())

for key in stud:            # looping in dictionary
    print(key)

for key, value in stud.items():
    print(key, value)
