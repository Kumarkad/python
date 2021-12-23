'''
Write a Python program to store second year percentage of students in 
array. 
Write function for sorting array of floating point numbers in ascending 
order using
a) Insertion sort
b) Shell Sort and display top five scores
'''
def insertion_sort(marks):
    for i in range(1,len(marks)):
        key=marks[i]
        
        j=i-1
        while j>= 0 and key <marks[j]:
            marks[j+1]= marks[j]
            j-=1
            marks[j+1]=key
            
    print(" Marks of students after performing insertion sort : ")
    for i in marks:
        print(i)
    
def shell_sort(marks):
    gap=len(marks)//2
    
    while gap >0:
        i=0
        j=gap
        
        while j< len(marks):
            if marks[i]>marks[j]:
                marks[i],marks[j] = marks[j],marks[i]
            
            i +=1
            j +=1
            
            k = i
            
            while k - gap > -1:
                if marks[k-gap] > marks[k]:
                    marks[k-gap],marks[k] = marks[k],marks[k-gap]
                
                k-=1
                gap//=2
                
    print(" Marks of students after performing shell sort : ")
    for i in marks:
        print(i)
    
def top_five_marks(marks):
        print(" Marks of top five scores are : ")
        marks.reverse()
        print(marks[:6])
            
marks=[100,30,60,70,54,23,19,20,35,5]
'''
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students : ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element
'''
print("The marks of",'n',"students are : ")
print(marks)

insertion_sort(marks)

shell_sort(marks)

top_five_marks(marks)