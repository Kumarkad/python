'''
Write a Python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using
a)SelectionSort 

b) Bubble sort and display top five scores.
'''

def selection_sort(marks):
    for i in range(len(marks)):
        
        min_ele=i
        for j in range(i+1,len(marks)):
            if marks[min_ele]>marks[j]:
                min_ele=j
                
        marks[i],marks[min_ele]=marks[min_ele],marks[i]
    print(" Marks of students after performing selection sort : ")
    for i in marks:
        print(i)

def bubble_sort(marks):
    for i in range(len(marks)-1):
        for j in range(0,len(marks)-i-1):
            if marks[j]> marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    print(" Marks of students after performing bubble sort : ")
    for i in marks:
        print(i)
        
def top_five_marks(marks):
        print(" Marks of top five scores are : ")
        marks.reverse()
        print(marks[:6])
            
marks=[]

n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students : ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element

print("The marks of",'n',"students are : ")
print(marks)

selection_sort(marks)

bubble_sort(marks)

top_five_marks(marks)