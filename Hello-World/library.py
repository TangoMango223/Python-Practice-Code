# Practice using libraries.
#Sources: https://www.tutorialspoint.com/python3/python_strings.htm


#First, practice getting strings
s = str(input("What's your name?: "))
print(f"Nice to meet you {s}!")

# Comparing strings - much easier.
#use s.lower() to evaluate cases too.
a = str(input("Do you agree?: "))

if a.lower() == "y":
    print("Agreed!")
else:
    print("Not agreed.")

#Cough using function. Use the main function to call it!
# Throw everything under def main
def main():
    for i in range(3):
        cough()

#Define functions
def cough():
        print("Cough!")

main()

# #Call Coughing - version #1
# def ncough(n):
#     for i in range (n):
#         print("Cough!")

# ncough(3) //call the coughing function 

#Call Cough using main function 



