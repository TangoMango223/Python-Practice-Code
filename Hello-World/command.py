#Finally, let's explore Command Line arguments

from sys import argv

# for i in range(len(argv)):
#     print(argv[i])

#Ignore the first argument and just print the stuff after
# i = 1
# length = len(argv) #calculate how many arguments there are
# for i in range(1,length):
#     #note: we use range because it "forces" a recognition of a collection of stuff, in this case, arguments
#     print(argv[i]) #start at 2nd argument

#Implement the exit code

if len(argv) != 2:
    print("Wrong usage! Try again.")
    exit(1) #exit with 1 means there was an error. equal to "Return true"
else:
    print(f"Nice to meet you, {argv[1]}!")



