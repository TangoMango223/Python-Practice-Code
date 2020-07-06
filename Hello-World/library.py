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

#Define functions
def cough():
        print("Cough!")

#Cough using function
for i in range(3):
    cough()