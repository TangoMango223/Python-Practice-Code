#Let's get a positive integer

import math #let's use this

#Ask for an input
def get_positive_int():
    while True:
        positive = int(input("Give me a positive integer: "))
        if positive > 0:
            break
    return positive #very important to have a return, otherwise python won't see anything. 
    #return is equal to the result that is provided when the function is done.

def main():
     i = get_positive_int() #will only work if "return positive" is there, and a variable to store it. 
     print(f"You gave me {i} as a positive integer. Is this correct?")

'''
Using functions to do this and storing in variables is known as pass by value. 

but it's only in the function level so in the main code level, it doesn't remember i 
Three single-quotation marks  is used to denote multi-line comments '''

#main()

#i = 10
# print(f"Example of different scopes: i is equal to {i} here. \
# I is different from your function since we didn't do pass by reference or value.")

#Example: Pass by Value in Python
a = 0 #use this to store
a = get_positive_int()

b = 0 # use this store the value 
b = a #save the value of 

a = a +3 #add 3 to the number

print("Notice how a and b have different values. That's because of pass by value:")
print(f"a is {a} and b is {b}! Very different numbers, because I added 3 to a, making it higher.")





