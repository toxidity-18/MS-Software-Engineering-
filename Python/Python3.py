# Remember attention to detail at all times #

# Learning python 3 

# using print 
print('Hello world')
print('Am learning python bit by bit .')

# testing the # symbol
 # using it as a comment 
# this code will print Hey am a python programmer 
print('Hey am a python programmer')
# this code won't print anything #print('Python as a backend language)
# print('Python as a backend language)

# Numbers and math 
# + plus , - minus , / slash , * asterisk , % percent , < less than <= less than equal to , > great than , >= greater than equal to 

25 + 30 / 6 # 30.0
100 - 25 * 3 % 4 # 97
3+2<5-7
# meaning of the word modulus and how it work 

# variables and names 
car = 100
passenger = 90
space_in_car = 4.0
driver = 30
car_not_driven = car - driver
car_driven = driver  
carpool_capacity = car*space_in_car 
average_passenger_per_car = passenger / car_driven 

print('There are', car ,'cars available.') # remember anytime we put variables inside print statements make sure to use comma 
print('There are',driver,' drivers available.')
print("There will be", car_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passenger, "to carpool today.")
print("We need to put about", average_passenger_per_car,
"in each car.") #variable within print statements are replaced with their respective values 

# format strings 
my_name = 'Zed A Shaw'
my_age = 35
my_height = 74 
my_weight = 180 
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f'Let\'s talk about {my_name}') #{} used to place  the value of variables 
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f'His teeth are usually {my_teeth} depending on the coffee')
# tricky piece of code 
total = my_age + my_height + my_weight 
print(f'If I add {my_age},{my_height} and {my_weight} i get {total}')

# inches into centimeters and pounds into kilograms 
# using mathematical expressions in python etc 

# strings and text 
types_of_people = 10
# f string for formatting various string methods 
# print which results to print of different values 
x=f'There are {types_of_people} types of people '
binary = 'binary'
do_not = "don't"
y=f'Those who know {binary} and those whe {do_not}.'
print(x)
print(y)
print(f'I said:{x}')
print(f'I also said:{y}')
hilarious = False
joke_evaluation = 'Isn\'t that joke so funny ! {}'
print(joke_evaluation.format(hilarious)) # f string works the same way as .format() method   format, formatter.format formatter.format ...
w = 'This is the left side of ...'
e = 'a string with a right side'
print(w+e)

# print f string format string 
print('Mary had a little lamb')
print('It\'s fleece is white as {}.'.format('snow'))
print('Everywhere that Mary went')
print('.'*10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1+end2+end3+end4+end5+end6,end='')
print(end7+end8+end9+end10+end11+end12)

# printing printing 
# meaning of formatter and what it does 
formatter='{} {} {} {} ' # acts as a placeholder .
print(formatter.format(1,2,3,4))
print(formatter.format('one','two','three','four'))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
  'Try your',
  'Own text here',
  'Maybe a poem',
  'Or a song about fear'
))

# 
days = 'Mon Tue Wed Thur Fri Sat Sun'
months = '\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nNov\nDec\n'
print('Here are the days:',days)
print('Here are the months:',months)
print(
  '''
there something going on here 
with three double/single quotes
will we be to type as much as we like
even 4 lines or 5 or 6'''
)
# trying something fun 
tabby= "\tI'm tabbed in" # \t \n \t \n 
persian_cat="I'm split\non a line" # what is split\non 
backlash_cat ="I'm \\ a \\ cat"
fat_cat = """
I'll do a list:
\t*Cat Food
\t* Fish
\t* Catnip\n\t* Grass
"""
print(backlash_cat)
print(tabby)

# 25 | jun | 2025
name ='\bSam \bGic'