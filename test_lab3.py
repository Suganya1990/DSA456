#   Author: Catherine Leung
#   These are the unit tests for functions and classes of lab 3
#   To use this, run: python test_lab3.py
#   Tested using Python 3
#

import unittest
#from lab3 import factorial,linear_search,binary_search

#recursive function to determine factorial returns a number
def factorial(number):
    if number == 0 :
        return 1
    return number*factorial(number -1)

def linear_search(list, key):
    index = len(list)
    val =  linear_search_recurrsion(list,key,index)
    return val
    

def linear_search_recurrsion(list, key, index):
        if(index == 0):
            return -1
        elif(list[index-1]==key):
            return index-1
        return linear_search_recurrsion(list, key, index-1)
        
def binary_search(mylist, key):
    return binary_search_recurrsion(mylist, 0, len(mylist)-1, key)

def binary_search_recurrsion(myList, minIndex, maxIndex, key):
    if  maxIndex >= minIndex:
        #get middle index of the array 
        middleIndex= minIndex + (maxIndex-minIndex)//2
        if(myList[middleIndex]==key):
            return middleIndex
        elif myList[middleIndex]<key:
           return binary_search_recurrsion(myList,  middleIndex+1, maxIndex, key)
        elif myList[middleIndex]>key:
            return  binary_search_recurrsion(myList, minIndex, middleIndex-1, key)
    #not inside the list
    else:
        return -1
    

    

class Lab1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab3"""
    
    def test_linear_search(self):
        mylist = [34, 1, 18, 20, 25, 30, 15, 16, 17, 22, 24, 31, 163, 9, 33, 55]
        self.assertEqual(linear_search(mylist,0), -1)
        self.assertEqual(linear_search(mylist,19), -1)
        self.assertEqual(linear_search(mylist,164), -1)
        curr = 0
        for i in mylist:
            self.assertEqual(linear_search(mylist,i),curr)
            curr+=1

    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(19),121645100408832000)
        self.assertEqual(factorial(8),40320)


    def test_binary_search(self):
        mylist = [1, 2, 4, 5, 8, 10, 15, 22, 27, 29, 30, 33, 55, 81, 100, 108, 200, 205, 310, 315]
        self.assertEqual(binary_search(mylist,0),-1)
        self.assertEqual(binary_search(mylist,19),-1)
        self.assertEqual(binary_search(mylist,201),-1)
        self.assertEqual(binary_search(mylist,320),-1)
        curr = 0
        for i in mylist:
            self.assertEqual(binary_search(mylist,i),curr)
            curr+=1


 
if __name__ == '__main__':
    unittest.main()



# Function 1 Analysis : The time complexity  would be  T(n-1) becuase it will have to iterate through the function  number-1 times. If number is 100 the function will have to go through 99 times (number-1).

#Funcion 2 Analysis: I think the time complexity would be O(log n). This is similar to binary search, where each iteration will cut the length by half. 



#Reflection 
#1
#Describe how to approach writing recursive functions; what steps do you take? I approach recursive function by first determinging the base case the exit. Then I created the recursive function call inside the function. Then I determine where to place
#  the recursive funciton to ensure it works. Finally test the function. 

#2 
#I think the analysis for the recursive funcion is the same as any other function. I still evalute the worst possible case like I would any other function for time compleixity.