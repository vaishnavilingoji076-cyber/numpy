arr=[1,2,3]
n=len(arr)

for start in range(n):
    for end in range(start, n):
        print(arr[start:end+1])