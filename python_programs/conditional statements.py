
# if statement

language = 'Python'
if language == 'python':
    print('Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Please logg in')

if not logged_in:
    print('Logg in')
else:
    print('Logeed in')

A = [1,2,3]
B = [1,2,3]
print(A,B)
print(A is B)
print(id(A))
print(id(B))
A = B
print(id(A))
print(id(B))

condition = False
if condition:
     print('Evaluated to True')
else:
    print('Evaluted to False')

condition = None
if condition:
     print('Evaluated to True')
else:
    print('Evaluted to False')

condition = 0
if condition:
     print('Evaluated to True')
else:
    print('Evaluted to False')

condition = {}
if condition:
     print('Evaluated to True')
else:
    print('Evaluted to False')

condition = A
if condition:
     print('Evaluated to True')
else:
    print('Evaluted to False')

