arr=[10,20,30,40,50]
print(len(arr))

arr=["apple", "banana","mango"]
print(arr)

arr=[10, "hello", 3.5]
print(arr)

vaish=[1,2,3,4]
print(vaish[0])
print(vaish[-2])
print(vaish[-1])

#updating elements

arr=[10,20,30]
arr[1]=100
print(arr)

#traversing an array

arr=["vaish","shweta","pari"]

for i in range(len(arr)):
    print(arr[i])

#inserting elements

arr=[90,80,70]
arr.append(60)
print(arr)

#at any position
arr.insert(1,21)
print(arr)

#deleting elements
arr.remove(60)
print(arr)

#removing by index
arr.pop(1)
print(arr)

#delete
del arr[0]
print(arr)

#all clear
arr.clear()
print(arr)