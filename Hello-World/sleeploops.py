#Other useful coding techniques to know

#Use the sleep function to slow down counting
from time import sleep

#While Loop - There will never be a stack overflow because Python doesn't have pointer or memory issues
i = 2
while True:
    i = i**2
    print(i)
    sleep(1)
    if i == 340282366920938463463374607431768211456:
        break #let's stop it before it goes insane.





