A1,B1=map(int,input(" ").split(" "))
C1=[]
for i in range(A1+1,B1+1):
    if(i%2!=0):
     C1.append(i)
print(*C1,sep=" ")
