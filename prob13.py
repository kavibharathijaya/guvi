A1=int(input(" "))
if A1>1:
    for i in range(2,A1):
        if A1%i==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
