# Practice code from CS50 Harvard course
# source: https://cs50.harvard.edu/x/2020/notes/6/

# Basics:
print("hello, world!")

#Hello World combining strings
answer1 = input("What's your name? \n") #use input
print("Hello " + answer1 + "!")

#Practice printf
answer2 = input("What's your dog's name? \n")
print(f"Your dog's name is {answer2}!n")

#use print(f ____ {}) format to quickly refer to variables

#Just like C Language, \n means new line. 

#Conditions be like:
x = input("Give me a number for X \n")
y = input("Give me a number for Y \n")

if x<y:
    print("X is Less than Y")
elif x>y:
    print("X is greater than Y")
else:
    print("X is equal to Y")

