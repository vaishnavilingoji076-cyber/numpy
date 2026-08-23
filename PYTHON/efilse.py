#if else

age=20

if age>=18:
    print("Eligible")
else:
    print("non Eligible")

#The if statement executes code only when the condition is True.
age=20

if age>=18:
    print("Adult")

age=15
if age>=18:
    print("adult")

#if-elif-else
marks=86

if marks>=90:
    print("A+")

elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
else:
    print("Fail")

#using And
age=25
has_license=False

if age>=18 and has_license:
    print("Eligible")
else:
    print("not Eligible")

#using Or
day="sunday"
if day== "saturday" or day=="sunday":
    print("weekend")
else:
    print("working day")

#nested if
age=25
has_id=True

if age>=18:
    if has_id:
        print("entry allowed")
    else:
        print("ID REQUIRED")
else:
    print("you are under 18")

#if with strings

username="vaishnav"

if username=="vaishnav":
    print("welcome vaishnav")
else:
    print("Invalid user")


#if with numbers
number=-1

if number>0:
    print("positive")
elif number<0:
    print("negative")
else:
    print("zero")

#checking even or odd
number=5

if number%2==0:
    print("Even")
else:
    print("odd")