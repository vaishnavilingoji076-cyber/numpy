#join() it joins multiple lists togather

worlds=["vaishnav", "is", "mine"]
result=" ".join(worlds)

print(result)


vaishnav=["vaishnavi", "is", "mine"]

result=" ".join(vaishnav)
print(result)

#find()Returns the index of the first occurrence.

text="vaishnav"
print(text.find("v"))

#startswith() Checks whether a string starts with something.

text="python programming"

print(text.startswith("python"))
print(text.startswith("rutvik"))
print(text.endswith("programming"))

#isdigit()

#Checks whether all characters are digits.

text="12345ab"
print(text.isdigit())

#isalpha()
#Checks whether all characters are alphabetic.

text="vaishnav"

print(text.isalpha())

#partition() divides a string into three parts:

text="hello-vaishnav"
print(text.partition("-"))

#splitlines() Splits a string at line boundaries.

text="hello\nvaishnav\ni\nlove\nyou"
print(text.splitlines())

#centre Centers a string within a specified width.
text = "Python"

print(text.center(20))