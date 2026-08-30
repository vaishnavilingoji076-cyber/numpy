#A string is a sequence of characters enclosed inside quotes.

#A string in Python is an immutable sequence of Unicode characters used to represent textual data.
#Immutable means once a string is created, its individual characters cannot be changed.

name="vaishnav"
print(name[5])
print(name[-1])

#Slicing allows you to extract part of a string.
print(name[0:5])

reverse=name[::-1]


#len returns the num of characters

v="vaishnavi"
print(len(v))

#concat
f="hey"
s="vaishnavi"

result=f+ " "+s
print(result)

text="hi"
print(text*3)


text="vaishnavi"
print("m" in text)

