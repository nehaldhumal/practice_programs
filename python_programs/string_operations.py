# Print Welcome Message
print('Welcome To Python')

# creating Textual Data
message = 'Hello! This is Nehal'
print(message)

# creating textual data using double quotes
my_message = "Booby's World"
my_message1 = 'Bobby\'s World'
print(my_message,my_message1)

# creating multi line string
my_message2 = """Hello This "is" Booby's World"""
print(my_message2)

# Length function
message = 'Hello World'
print(len(message))
# Accessing strings character individually
print(message[0:5])
print(message[6:]) # This is called slicing

# Lower And Upper Case Function
print(message.lower())
print(message.upper())
# Count and Find Function
print(message.count('l'))
print(message.find('World'))

# Replace Function
message = 'Hello World'
new_message = message.replace('World', 'universe')
message = message.replace('universe', 'world')
print(new_message)
print(message)

# How to add multiple strings and concatinate them together

greeting = 'Hello'
name = 'Michael'
message = greeting + name
message = greeting + ' ' + name
message1 = greeting + ', ' + name + '. Welcome!' #complicated
print(message)
print(message1)
message2 = '{}, {}. Welcome!'.format(greeting, name) #Placeholders
print(message2)

# f strings (you can  write name in all caps)
message2 = f'{greeting}, {name}. Welcome!'
message2 = f'{greeting}, {name.upper()}. Welcome!'
print(message2)
