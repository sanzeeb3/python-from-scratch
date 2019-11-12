#Printing Hello World.
print("Hello World")

#Condition check. Intendation is used to indicate a block of code. Intendation in python is not only for readability.
if 5 > 2:
    print("Five is greater than two!")

#Variables.
x = 190
print(x)

#Assigning values to multiple variables.
x, y, z = 'Orange', 'Banana', 'Pineapple'
print(y)    #Prints Banana.

print(y+' is a fruit')

#+ can also be used as a mathematical operator.
x, y = 5, 10
z = x+y
print(z)

def myfunc():
    print(x)    #x is also defined here. These are global variables. Can be used inside a function.

myfunc()

def myfunc():   #same function name doesnot result in error.
    x = 'Good'
    print(x)    

print(x)
myfunc()

def myfunct():
   global x = 'bad' #variable declared withnamespace global.
   print(x)

print(x)    #Output bad.

print(type(x))  #Prints datatype.

x = str('Hello World!')
x = ['apple', 'orange', 'banana']  #list datatype.
x = ('apple', 'orange', 'banana')  #tupple datatype.
x = {"apple", "banana", "cherry"}  #set datatype.

#More datatypes here and description: https://www.w3schools.com/python/python_datatypes.asp

#Numbers
#Casting x = int(2.8) Outputs 2.


#Strings are arrays.
x = 'Hello World!'
print(x[1])   #Prints e.

#Lists.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Prints the last item of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Returns the third, fourth, and fifth item:

#More on lists: https://www.w3schools.com/python/python_lists.asp
# Loop through a list.
# Check if item exists.
# List Length.
# Add itmes.
# Remove items. etc.


