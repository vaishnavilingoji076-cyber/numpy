fruits=["apple" , "banana", "mango"]

fruits[1]="kiwi"
print(fruits)

#adding elements
numbers=[10,20,30]
numbers.append(40)
print(numbers)


v=["chiu ","guddi"]
v.append("vaishnav")
v.append("rugved")
print(v)

#insert() adds an element at a specific position.

#list.insert(index, value)
numbers=[1,2,3]
numbers.insert(3,70)
print(numbers)


names=["chiu", "guddi"]
names.insert(3,"rugved")
names.insert(4,"vaishanv")
print(names)

#extend() adds multiple elements to the end of a list.

numbers=[1,2,3]
numbers.extend([7,8,9])
print(numbers)

#remove() removes an element by its value.
numbers=[1,2,3,4,5,6]
numbers.remove(3)
print(numbers)

#pop() removes an element using its index and returns that element.
numbers=[1,2,3,4,5]
x=numbers.pop(2)
print(x)
print(numbers)

#If you don't provide an index, pop() removes the last element.
numbers=[1,2,3]
numbers.pop()
print(numbers)

#del can also remove elements.
numbers=[1,2,3,4,5]
del numbers[1]
print(numbers)

numbers=[10,20,30,40,50]
del numbers[2:4]
print(numbers)

#clear() removes everything from the list.
numbers=[1,2,3]
numbers.clear()
print(numbers)

#index() tells you the position of an element.
fruits=["apple","banana","cherry"]
v=fruits.index("cherry")
print(v)


v="vaishnavi"
position=v.index("h")
print(position)
print(v.count("i"))


#count() tells you how many times a value appears.
numbers=[10,20,30,40,20,20]
print(numbers.count(20))

#sort() arranges the list.
numbers=[9,5,9,0,3,6]
numbers.sort()
print(numbers)

#By default, it sorts in ascending order.
numbers=[50,30,80,90,10]
numbers.sort(reverse=True)
print(numbers)

#reverse() reverses the order of the list.
numbers=[1,2,3,4,5]
numbers.reverse()
print(numbers)

#copying a list
numbers=[10,20,30]
new_numbers=numbers.copy()
print(new_numbers)

#two separate lists
numbers=[10,20,30]
new_numbers=numbers.copy()
new_numbers.append(40)

print(numbers)
print(new_numbers)

