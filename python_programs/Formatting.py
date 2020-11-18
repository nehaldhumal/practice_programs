
person = {'name': 'john', 'age': 23}
sentence1 = 'My name is' + person['name'] + ' and my age is ' + str(person['age']) + ' years old. '
sentence2 = 'My name is {0}. And my age is {1}'.format(person['name'],person['age'])
sentence3 = 'My name is {0[name]}. And my age is {1[age]}'.format(person,person)
sentence4 = 'My name is {name} and my age is {age}'.format(**person)
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)
tag = 'h1'
text = 'This is sentence'

sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('John','23')            # creating instance of the class person
sentence = 'My name is {0.name}. My age is {0.age}'.format(p1)
print(sentence)

sentence = 'My name is {name}. My age is {age}'.format(name='john',age='23')
print(sentence)


# Unpacking from dict

course = {'c_name': 'Psychology', 'c_subj': 'Human Psych'}
sentence = 'The name of the course is {c_name}. Material name in the course is {c_subj}'.format(**course)  # unpacking dict course
print(sentence)

# formatting nos

for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)
    sent = 'The value is {:02}'.format(i)
    print(sentence)


sent = '1 mb is equals to {:,.2f} bytes'.format(1000**2)
print(sent)