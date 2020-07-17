#Mario-Less, make a small half triangle
# From here: https://cs50.harvard.edu/x/2020/psets/6/mario/less/

import sys #for exit

#Get height
height = int(input("Give me a height: ")) #cast as int
if (height < 1 or height > 8):
    print(f"Your height, {height} does not fit the parameters of 1-8. Please try again")
    exit(1)

#Print the height:
print(f"Height: {height}")

#Print the Mario Triangle - Left Aligned!
print("-----------Left Aligned-------------")
for i in range(height):
    for j in range(0,i+1):
        print("#", end = "")
    print()

#Print the Mario Triangle - Right Aligned now!
print()
print("-----------Right Aligned-------------")
for i in range(height):
    for j in range(0,i+1): #needs to be opposite
        print("#", end = "")
    print()
