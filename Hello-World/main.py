#While Python has no main function, you can use it to help functions without bringing them to the top of your code

#Let's make a function that adds two numbers together
def add(x, y):
    z = x + y
    print(f"The sum of {x} and {y} is {z}")

#Now, let's make a main function to call it. 
def main():
    add(10,5)

#Abstraction and etc. at the bottom
main()




