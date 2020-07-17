#Python can swap values without passing by reference, like in C.

a = 1
b = 2

print(f"Before, a was {a} and b was {b}! Now... ")
a,b = b,a #swap without a container
print(f" b is {b} and a is {a}!")
