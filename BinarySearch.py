#Author: Dustin Kaban
#Date: February 10th, 2020
#MIT LICENSE

#Random import is only to input random numbers into the function for testing
import random

#Binary Search Algorithm - Finds a value in an array by diving the list in half continually until the value is found
#Designed for a sorted list
def BinarySearch(array,val):
    #We want to exit the function right from the start if the value inputted is invalid
    if (val > len(array)):
        print("Value of " + str(val) + " not found")
        return
    min = 1
    max = len(array)+1
    while(min <= max):
        guess = int((min+max)/2)
        if(guess == val):
            print("Success! Array Contains Value of " + str(guess))
            return guess
        elif(val > guess):
            min = guess+1
        else:
            max = guess-1

    print("Value Not Found")
    return 0

#Data created purely for testing the function
valArray = [1,2,3,4,5,6,7,8]
val = int(random.randrange(1,10))
BinarySearch(valArray,val)