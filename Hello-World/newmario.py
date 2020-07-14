# Repeating some of the basic Mario instructions from the early C projects

#Print 4 lines of ? as with the Mario blocks
print("-----------------")
print("Print a row of ?????")
for i in range (4):
    print("?", end = "") #use end = "" to stop each row from printing a new line.
print()

#Print a column of hashtags:
print("-----------------")
print("Print a column of hashtags:")
for i in range (3):
    print("#")

#Print a box of # too:
print("-----------------")
print("Print a box of #:")
for i in range(3):
    for j in range(3):
        print("#", end = "")
    print() 


