#A for loop is used when you know how many times you want to repeat something or when you want to iterate through a collection (like a list, tuple, string, dictionary, etc.).

fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)


for i in range(5):
    print(i)

#two argumemnts
for i in range(4,9):
    print(i)


word="vaishnav"
for i in word:
    print(i)


numbers=(10,20,30)

for num in numbers:
    print(num)

#looping through a set

colors={"v,g,o"}
for i in colors:
    print(i)

#looping through a dictionary
chiu={
    "name":"vaishnav",
    "age":21,
    "designation":"software developer"
}

for i in chiu:
    print(i)

#to get values
for values in chiu.values():
    print(values)

#to get both
for i, values in chiu.items():
    print(i,values)


#while loops
#A while loop repeats as long as a condition is True.

count=1

while count<=5:
    print(count)
    count +=1

#break statement
#Stops the loop immediately.

for i in range(10):
    if i==7:
        break
    print(i)

#continue
#Skips the current iteration and moves to the next one.

for i in range(6):
    if i == 7:
        continue
    print(i)

