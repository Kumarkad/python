# check whether list is in hill valley or not

list=[]

n=int(input("how many elements do you want to add in list : "))
for i in range(0,n):
  a=int(input("Please Enter The element :"))
  list.append(a)
  
list1=list.copy()
list2=list.copy()
print(list)

k=list.__len__()//2

for i in range(1,k+1):
		if list1[k] > list1[k-i]:
			list1[k]=list1[k-i]
			up=True
		else:
			up=False
		if up==False :
			break
			
for i in range(1,k+1):
		if list2[k] > list2[k+i]:
			list2[k]=list2[k+i]
			down=True
		else:
			down=False
		if down==False :
			break
		
if up==down==True:
	print("List is in Hill Valley ")
else:
	print("List is not in Hill Valley")
