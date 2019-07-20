giv=str(input(" "))
count=0
for n in giv:
    if n.isnumeric() or n.isalpha():
        pass
    else:
        count+=1
print(count)
