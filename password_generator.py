from distutils.log import error
import numbers
import random
import string

count_frontend = int(input("I would like this many characters in my password: "))
count_backend = int(count_frontend) // int(2)
letters = string.ascii_letters
letters2 = string.punctuation

if count_frontend < 8:
    print("Your password has to be at least 8 characters long!!")
elif count_frontend > 40:
    print("Your password cannot be longer than 40 characters!!")
else:
    print("".join(random.choice(letters) for i in range(count_backend)), "".join(random.choice(letters2) for i in range(count_backend)))
