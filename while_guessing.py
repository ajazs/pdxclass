'''while loop version if guessing game.
psuedo code: import randint, maybe come up with a integer prior to entering loop. then modifying it to do it inside
use if statements inside loop
where input == comp
print "you match"

add a counter later.'''

import random
num = random.randint(0,10)
user = int(input("give me a number"))
count = 1
print(num)
while user != num:
    user = int(input("give me another number "))
    count += 1

print("match")
#print(count)
if count == 1:
    print("You got it on the first try!")

else:
    print(("it took you"),count,("tries"))
