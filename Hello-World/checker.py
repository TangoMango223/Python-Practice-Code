#Implement Code to check if Emma is in the list

import sys #Need it for exit code

cohort1 = ["Emma", "Christine", "Kevin", "Garima"]

#Check if cohort 1 has Emma
look = input("Who are you looking for in Cohort 1?: ")

if look.capitalize() in cohort1:
    print(f"Found {look.capitalize()}!")
    sys.exit(0)
else:
    print(f"Did not find {look.capitalize()}. Sorry!")
    sys.exit(1)