
# List Comprehensions
nums = [1,2,3,4,5,6,7,8,9,10]

# I want n for each n in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# using list comprehensions
my_list = [n for n in nums]
print(my_list)

# n*n
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

# using lc
my_list = [n*n for n in nums]
print(my_list)

# using maps and lambda
my_list = list(map(lambda n: n*n, nums))
print (my_list)

# even no

my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

# using ls
my_list = [n for n in nums if n%2 == 0]
print(my_list)

# using map and filter
my_list = list(filter(lambda n: n%2 == 0, nums))
print(my_list)

# letter no pair for each letter 'abcd' for each num '0123'

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)

# using comprehensions
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

# comprehensions in Dictionary

name = ['Bruce','Peter','Jack']
heros = ['Batman','Spiderman','Superman']
# print(zip(name,heros))

my_dict = {}
#for name, hero in zip(name,heros):
#    my_dict[name] = hero
#print(my_dict)

# using comp

my_dict = {name: hero for name,hero in zip(name,heros)}
print(my_dict)

my_dict = {name: hero for name,hero in zip(name,heros) if name != 'Peter'}
print(my_dict)

# sets

nums = [1,1,2,3,2,4,2,1,6,8,5]
#my_set = set()
#for n in nums:
#    my_set.add(n)
#print(my_set)

# Generator functions
# using comp
my_set = {n for n in nums}
print(my_set)

num = [1,2,3,4,5,6,7,8,9,10]
def gen_func(num):
    for n in num:
        yield n*n

my_gen = gen_func(num)

for i in my_gen:
    print(i)

# using comp
my_gen = (n*n for n in num)
for i in my_gen:
    print(i)