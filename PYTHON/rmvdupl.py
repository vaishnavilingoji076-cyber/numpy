arr=[1,1,2,3,4,4,5]

result=[]

for num in arr:
    if not result or result[-1] !=num:
        result.append(num)

print(result)
