'''
Write a Python program to compute following operations on String: 
a) To display word with the longest length 
b) To determines the frequency of occurrence of particular character in the string 
c) To check given string is palindrome or not 
d) To display index of first substring 
e) To count the occurrences of each word in string
'''
sentence=input(" Enter sentence : ")

#To display word with the longest length

long = max(sentence.split(), key=len)
print("Longest word is: ", long)
print("And its length is: ", len(long))

#To determines the frequency of occurrence of particular character in the string 

freq={}
for i in sentence:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
print("Count of all characters in sentence is :\n "
      + str(freq))

#To check given string is palindrome or not 

word=input('Enter  String to check is palidrome or not :')
print(" given word is : ",word)
rev=reversed(word)
if list(word)==list(rev):
    print("string is palidrome")
else:
    print("string is not palidrome")

# To display index of first substring 

sub_str1 =input("Enter word : ")
print("index of first appearance of the substring "+sub_str1+" is")
print(sentence.find(sub_str1))

#To count the occurrences of each word in string

words=sentence.split()
print(words)
str=[]
for i in words:
    if i not in str:
        str.append(i)
    
for i in range(0,len(str)):
    print('count of occurrences ',str[i],' is ',words.count(str[i]))