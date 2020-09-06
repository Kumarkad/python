ls=[]
n=int(input("how many elements do you want to add in list : "))
for i in range(0,n):
  a=int(input("Please Enter The element :"))
  ls.append(a)
l1=[]
l2=[]
a=len(ls)
m=int(a/2)
for i in range(1,m):
  min=ls[m-i]
  max=ls[m+i]
  l1.append(min)
  l2.append(max)
if l1==l2:
  print("list is in hill valley")
else:
  print("list is not in hill valley")
