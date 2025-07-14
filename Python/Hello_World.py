print('Hello Python World !') 

# variables 
message = 'Hello Python World!'
print (message)

message1 = 'Hello python crash course world !'
print (message1)

# NB : Python will always keep track of the current value of its variable 

# naming error in python 
message2 = 'Example of a naming error'
# print(mesage2)  : This will create the Name Error 
print(message2)

# message3
# print(message3)

# simple exercise 
programming_language = 'Python'
print(programming_language)
programming_language = 'Flask'
print(programming_language)

# DATA TYPES 

# Strings  
'This is a string'
"This is a string"

# NB: Using quotes inside of quotes  and apostrophes 
' I told my friend that , "Python is my favorite programming language."'
"The language 'Python' comes from Monty Python and not the snake."
"One of Python's strengths  is it diverse and supportive community."

# Changing cases 
name = 'ada lovelace'
print(name.title())
# NB: Method : This is an action that Python can perform on a piece of data .
print(name.upper())
print(name.lower())

# Using variable inside a string 
first_name = 'Ada'
last_name = 'lovelace'
full_name = f' {first_name} {last_name}'  #NB: The f should out of the quotes thus to represent f-string and not inside the quotes .f for format .
print(full_name.title())
greetings  = f'Hello {first_name} {last_name}!'
print(greetings.title())
# using format()
full_name='{} {}'.format(first_name, last_name)
# practising the format() method 
creator = 'monty python'
creation = 'python programming language'
advantage = 'Diverse simple and easy to learn'
statement = '{} created {} which is {}'.format(creator.title(),creation,advantage.lower())

# WHITESPACES . NB Non-printing characters 
print('Python')
print('\tPython') # NB \t adds tab or space
print('Languages:\nPython\nC\nJavascript') # NB \n separates into newlines 

