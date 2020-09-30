#price =10
#print("10 is odd number:\n",10)
'''
vege = input("which teacher is very old : ")
food = input(" why : ")
print(vege," is old and walking fast ", food)
'''

'''
# CALACULATE THE YEAR OF BIRTHDAY
#---------------------------------
year_of_your_birth_day = int(input("Please Enter the year of your Birthday: "))
current_year = int(input("Please Enter the current year: "))
find_your_age = current_year - year_of_your_birth_day
print("Your age is :", find_your_age )
'''

#STRING

#course = " Python for Before "
#print(course[5])


'''
first = "John"
last = "Smith"
message = f'{first} {last} is a coder '
print(message)
'''

#STRING METHOD
#--------------
'''
name1 ="mpoyi "
name2 = "Ruth "
name3 = "Join "
name = name1+name2+name3
print(name)
'''
'''
# F Substutition
#------------------

book = "Python Book"
price = 1000

price_book = f"The book is {book} and the prise {price} rand "

#price_book = "The book is {} and the prise {} rand ".format(book, price)# old python version#

print(price_book)
'''

# METHOD OF STRING OR FUNCTIONS
#------------------ ------------
'''
name = 'frank'
new = name.capitalize() # convert the first name into capital letter
print(new)

name = 'FRANK'
new = name.casefold() # convert in lower case
print(new)


name = 'FRANK'
new = name.center(40) # center the name and random number for alignment
print(new)

name = 'FRANK'
new = name.center(40, "@") # center the name and random number for alignment and fill empty space with @
print(new)

name = 'FRANK'
new = name.endswith("K")# it return a boolean value
print(new)


name = 'FRANK'
new = name.startswith("f")# it return a boolean value
print(new)


description = 'frank Mpoyi is Python Developer in cape town '
new = description.find("Python") # find the position number of python in the string
print(new)

description = 'frank Mpoyi is Python Developer in cape town '
new = description.index("Python") # find the position number of python in the string same thing as above
print(new)

description = 'frank Mpoyi is Python Developer in cape town '
new = description.upper() # convert the string to upper case
print(new)


description = 'Frank Mpoyi is Python Developer in cape town '
new = description.lower() # convert the string to lower case
print(new)



description = 'Frank Mpoyi is Python Developer in cape town '
new = description.swapcase() # lower int upper and upper into lower case 
print(new)

description = 'Frank Mpoyi is Python Developer in cape town '
new = description.strip() # it removes unwanted white-space from string
print(new)




name = 'I love FRANK'
new = name.replace("FRANK", "PAULIN")# it replace the name
print(new)


name = 'I love FRANK'
new = name.split()# it will split the name
print(new)

description = 'Frank Mpoyi is Python Developer in cape town '
new = len(description) # it will print the length of the string
print(new)

'''
