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
#Remember, the range function is (start, stop, increment), where stop doesn't include the #
print()
print("-----------Right Aligned-------------")
for i in range(height):
    for j in range(1,height - i, 1): #prints white spaces for where there's nothing
        print(" ", end = "")
    for a in range(height-i, height+1, 1): #print the hashtags themselves
        print("#", end = "")
    print()

"""I learned from the code above that if you leave it as "" for print, it will ignore. 
You need a space in between."""

