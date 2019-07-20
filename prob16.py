A1,B1=map(int,input(" ").split(" "))
for x in range (A1+1,B1):
  for y in range (2,x):
    if (x%y==0):
      break
  else:
      print(x,end=" ")
