a=int(input(" "))
if(a==0):
    for i in range(0,5):
        print(0,end=" ")
else:        
    for j in range(1,(a*5)+1):
        if(j%a==0):
            print(j,end=" ")
