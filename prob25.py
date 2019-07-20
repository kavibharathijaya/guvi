p11=int(input(" "))
p21=list(map(int,input(" ").split(" ")))
p31=sorted(p21)
print(p31[p11//2])
