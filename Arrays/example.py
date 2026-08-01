
A = [2, 5, 8, 11]
B = [4, 7, 10, 13]

C = []
D = []

# Combine both arrays
for num in A + B:
    if num % 2 == 0:
        C.append(num)
    else:
        D.append(num)

print("Even numbers:", C)
print("Odd numbers:", D)