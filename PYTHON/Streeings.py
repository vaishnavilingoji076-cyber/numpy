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

#check element
text="vaishnavi"
print("m" in text)

name="python"

name=name.upper()
print(name)
name=name.lower()
print(name)

text="hello world"
print(text.capitalize)

#title capitalizes the first letter of each word

text="hello vaishnav"
print(text.title())

#swapcase() Changes uppercase characters to lowercase and lowercase characters to uppercase.

text="hello vaishnav"
print(text.swapcase())

#stripe() removes whitespace from the beginning and the end

text="  hello "
print(text.strip())

#lstrip()

#Removes whitespace from the left side.
text="  hello "
print(text.lstrip())
print(text.rstrip())

#replace() Replaces one piece of text with another.

text="i like java"
print(text.replace("java", "vaishnav"))

#split converts a string into list

text="apple bannan mango"
text=text.split()
print(text)
