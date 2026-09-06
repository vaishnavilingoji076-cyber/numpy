string="V*a*i*s*h*n*a*v"

v=""

for char in string:
    if char !="*":
        v=v+char

print(v)
    

#second method

string="V*a*i*s*h"

v=string.replace("*","")
print(v)