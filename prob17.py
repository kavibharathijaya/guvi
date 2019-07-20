a1=int(input(" "))
b1=a1
c1=0
while(b1>0):
   c1=c1+(b1%10)**3
   b1=b1//10
if(c1==a1):
  print('yes')
else:
  print('no')
