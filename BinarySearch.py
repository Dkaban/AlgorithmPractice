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
    #we set the array to start at 1 because if we started at 0 we'd have issues with the (min+max) calculation
    min = 1
    #Because we start at 1, we need to go the length of the array +1 to contain all items
    max = len(array)+1
    #We start with an initial guess in the middle of the array
    guess = int(min+max/2)
    while(min != max):
        if(guess == val):
            print("Success! Array Contains Value of " + str(guess))
            return guess
        elif(val > guess):
            #If the value inputted is greater than the guess, we want to set the min as guess
            #and then set guess as the average, then check again
            min = guess
            guess = int((max+guess)/2)
        else:
            #if teh value inputted is less than the guess, we want to set the max as guess
            #and then set guess as the average, then check again
            max = guess
            guess = int((min+guess)/2)

    print("Value Not Found")
    return 0

#Data created purely for testing the function
valArray = [1,2,3,4,5,6,7,8]
val = int(random.randrange(1,10))
BinarySearch(valArray,val)