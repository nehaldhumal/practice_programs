# Lists
# Create a list
course = ['Art', 'Science', 'Math', 'History']
print(course)
print(len(course))
print(course [0:2])
print(course[-1])
print(course[-2])

# Adding a item to list
course.append('ComSci')  # append method
print(course)

# Adding item to specific loc
course.insert(0,'Chemistry')
print(course)

# Merging two Lists
# add_courses = ['Geography', 'Pyschology']
# courses.insert(2,add_courses)
# print(courses)

# Removing items from list
course.pop()
print(course)
course.remove('Math')
print(course)

# Sorting a list

nums = ['4', '1', '6', '7']
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

sorted_nums = sorted(nums)   # sorted function
print(sorted_nums)


# Min, Max, Sum

print(min(nums))
print(max(nums))
# print(sum(nums))

# finding index of certain value

print(course.index('Art'))
print('Art' in course)             # in function

for courses in course:
   print(courses)

for index,courses in enumerate(course, start=1):
    print(index, courses)

# Join Method

course_str = ', '.join(course)
print(course_str)

course_str = ' - '.join(course)
print(course_str)

new_list = course_str.split(',')   #split fun
print(new_list)


# Tuples and Sets

List1 = ['Nehal', 'Raj']
List2 = List1

print(List1)

List1[0] = 'Ravi'
print(List1,List2)

List1.extend(List2)
print(List1)

# Mutable

item_1 = ['Math', 'History']
item_2 = item_1

print(item_1)
print(item_2)

item_1[0] = 'Art'
print(item_1)
print(item_2)

item_1.insert(0,'Science')
print(item_1)
# Immutable

tuple_1 = ('Math', 'History')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
print('Math' in tuple_1)
# tuple_1.insert(0,'Science')
# print(tuple_1)
# tuple_1[0] = 'Art'
# print(tuple_1)


# Sets --- They are unordered and are used to throw duplicate values

sub_1 = {'Math', 'English', 'Science'}
sub_2 = {'History', 'English', 'Chemistry'}
print(sub_1)
print('Math' in sub_1)

print(sub_1.intersection(sub_2))
print(sub_1.difference(sub_2))
print(sub_1.union(sub_2))

# Empty List

empty_list = []
empty_list = list()
print(empty_list)

# Empty Tuples

empty_tuple = {}
empty_tuple = tuple()
