#Arrays in Python

# In Python, LISTS = ARRAYS. They are dynamic, so no memory issues
# Tuples = like lists but they cannot change or cannot be amended.
# Lists = can be changed as often as you'd like

import math

#Make a blank array
scores = [] #lists

#Fill up with scores
scores.append(72) #assignment #1
scores.append(85) #assignment #2 score
scores.append(97) #assignment #3 scores

#Calculate average
average = round(sum(scores) / len(scores),1) #This works in python, as arrays are very smart.
print(f"The average is {average}! Great job!")

