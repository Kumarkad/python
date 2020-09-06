ov=[]
j=0
print("0. sort only odd numbers.")
print("1. sort only even numbers.")
b=int((input("Enter 0 or 1 : ")))
for i in ls:
  if i%2==b:
    a=ls.index(i)
    ei.append(a)
    ev.append(i)
    j=j+1
  else:
    ov.append(i)
print("Initial list is :")
print(ls)
ov.sort()
for i in range(0,j):
  k=ei[i]
  l=ev[i]
  ov.insert(k,l)
print("After the sorting your list :")
print(ov)
