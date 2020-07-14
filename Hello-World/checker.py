#Implement Code to check if Emma is in the list

import sys #Need it for exit code

cohort1 = ["Emma", "Christine", "Kevin", "Garima"]

#Check if cohort 1 has Emma
look = input("Who are you looking for in Cohort 1?: ")

if look.capitalize() in cohort1:
    print(f"Found {look.capitalize()}!")
else:
    print(f"Did not find {look.capitalize()}. Sorry!")

#Implement a dictionary; key and value

print("Let's try the phonebook to look for Emma:")
phonebook = { "Emma": "723-184-9321",
            "Christine": "638-172-1234"}

if "Emma" in phonebook:
    print(f"Emma's cell is {phonebook['Emma']}! Hope this helps.") #use single quotations in the middle, double outside
    sys.exit(0)
else:
    print("Nope sorry couldn't find Emma...")
    sys.exit(1) #anything not 0 is an error...