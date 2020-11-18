list = [5,3,1,4,2,7,6,8,9,10]
s_list = sorted(list,reverse=True)
print('Sorted List \t',s_list)
list.sort()
print(list)

# tuple   note - tuple doesnt have a sort method
tup = (6,5,4,2,3,1,9,3)
s_tup = sorted(tup)
print(s_tup)

# dict
di = {'name': 'Jack','job': 'Programmer','age': 23}
print(di)
s_di = sorted(di)
print(s_di)

# abs
li = [-4,-3,-2,1,2,3]
s_li = sorted(li)
print(s_li)
s_li = sorted(li, key=abs)
print(s_li)

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name,self.age,self.salary)

# from operator import attrgetter

e1 = Employee('Jack', 24, 50000)
e2 = Employee('Ray', 26, 60000)
e3 = Employee('Ben', 25, 450000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

s_employee = sorted(employees, key=e_sort)
#s_employee = sorted(employees, key=lambda e: e.name)
#s_employee = sorted(employees, key=attrgetter('age'))

print(s_employee)


