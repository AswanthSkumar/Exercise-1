#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Author      : Aswanth S
Date Created: 19/05/19
Description : Exercise 1
'''


# In[37]:


# Question 1

for x in range(2000,3201): #loop to take each number between 2000 and 3200
    if x%7==0 and x%5!=0:
        print(x,end=',')


# In[8]:


# Question 2
    
v=int(input("Enter Value to Find Factorial: "))
f=1
for x in range(2,v+1):  #loop to multiply each value from 1 to v 
    f*=x
print(f)
    


# In[9]:


# Question 3

v=int(input("Enter the Limit: "))
d={}                      #initializing an Empty dictionary to store values
for x in range(1,v+1):    #loop to calculate square of each no. btween the limit
    d[x]=x*x
print(d)


# In[16]:


# Question 4

v=int(input("Enter No of values to be inserted: "))
l=[]
for x in range(v):        #loop to input values
    y=int(input())
    l.append(y)           #adding values to the list
print(l)
print(tuple(l))           #using tuple() to copy all the elements from the list to the tuple 


# In[23]:


# Question 5

import math
s=str(input("Enter comma separated Integers: "))  
l=s.split(",")                                  #l is list used to store all the values in string format
l1=[]
for x in l:                                     #This loop is used to convert the inputed numbers from string to integer format  
    l1.append(int(x))                           #and store it in a new list l1
c=50
h=30
l2=[]
for d in l1:                                    # loop to calculate the values using the given formula
    l2.append(int(math.sqrt((2*c*d)/h)))
print(l2)


# In[25]:


# Question 6

s=str(input("Enter comma separated Integers: "))
l=s.split(",")                                  #storing values to a list 
l.sort()                                        #sorting the words
print(l)


# In[26]:


# Question 7

s="Hello world Practice makes perfect"
print(s.upper())
    


# In[31]:


# Question 8

s=str(input("Enter a string: "))
n=int(input("Enter the Number: "))
s1=""                                 #Initializing a new empty string to store the new string after deleting the character
for x in range(len(s)):               #To take each character and check if it is divisible by n
    if x%n!=0:
        s1+=s[x]
print(s1)


# In[34]:


# Question 9

n=[1,2,3,4,1]
if n[0]==n[len(n)-1]:          #Checking if First and Last element are equal
    print(True)
else:
    print(False)


# In[36]:


# Question 10

st=str(input("Enter Name: "))
age=int(input("Enter Age: "))
print("You will be 100 years old in ",100-age,"years")

