name="Vaishnav"
print(name)

x=10
print(type(x))

x=9.7
print(type(x))

#globle variable
#Create a variable outside of a function, and use it inside the function
v=" mine"

def myFunc():
    print("Vaishnav is" + v)

myFunc()


x=" mine"
def myFunc():
    x="fantastic"
    print("vaishnav is " + x)

myFunc()
print("vaishnav is"+ x)

#If you use the global keyword, the variable belongs to the global scope:
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x=" mine"
def myFunc():
    global x
    x="fantastic"

myFunc()
print("vaishnav is " + x)