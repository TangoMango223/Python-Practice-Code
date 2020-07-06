# Practice code from CS50 Harvard course
# source: https://cs50.harvard.edu/x/2020/notes/6/

#While loops
# no more while(true), it is now:

#Not going to run this loop since it will run forever.
# while True:
#     print("Hello world!")

#Another example: Cough 3 times. 
x = 0
print("---------")
print("Coughing via WHILE Loops: ")
while x < 3:
    print("Cough!")
    x = x +1

#Note: PRINT FUNCTION ALREADY GIVES A NEW LINE BY DEFAULT

#Write a for loop. Instead of for (int i....), it looks like this
print("---------")
print("Coughing via FOR Loops: ")
for i in [1,2,3]:
    print("Cough!")

# Lists in Python are like arrays in C. Lists = arrays
# They can grow and shrink without Malloc!
# Remember: [] is for lists, () for tuples, {} for dictionarys.
