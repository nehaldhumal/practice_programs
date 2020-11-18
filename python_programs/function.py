

# Functions

def hello_func():
    print('Hello Function.')
hello_func()
hello_func()
hello_func()
hello_func()

def hello_func():
    return 'Hello Function.'
print(hello_func())
print(hello_func().upper())
print('The length is:',len(hello_func()))

def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func('Hi'))

def hello_func(greeting,name,stmt='How are you'):
    return '{} {}. {}'.format(greeting,name,stmt)
print(hello_func('Hi','John'))

def stud_info(*args,**kwargs):
    print(args)
    print(kwargs)

stud_info('Math','Art', name='John', age=20)

def stud_info(*args,**kwargs):      # args and kwargs are conventions
    print(args)
    print(kwargs)

info = {'name': 'John', 'age':20}
courses = ['Math', 'Science']

stud_info(*courses,**info)


