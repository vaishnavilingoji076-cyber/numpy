string="vaishhnavv"
count={}

for char in string:
    count[char]=count.get(char,0)+1


for char in count:
    if count[char]>1:
        print(char)