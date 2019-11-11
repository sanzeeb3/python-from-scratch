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
   global x = 'bad' #variable declared withnamespace global
   print(x)

print(x)    #Output bad.
   
