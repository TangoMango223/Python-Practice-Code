#Python is powerful, has libraries to read files natively on Python:

import csv #library

file = open("phonebook1.csv", "a") #create a file called phonebook1, or open an existing one if exists

name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file) #calls file to write.
writer.writerow((name, number))

file.close() #close the file
