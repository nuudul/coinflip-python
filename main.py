import random


userin = None
userin = int(input("1 for tails, 2 for heads: "))
useropt = None
if userin == 1:
    useropt == True # for tails
elif userin == 2:
    useropt == False # for heads

x = random.randrange(1,100+1)
coin = None
if (x % 2) == 0:
    coin = True
elif (x % 2) == 1:
    coin == False

def coinflip(usr, pc):
    if usr == pc:
        return "Correct"
    elif usr != pc:
        return "Wrong"

print(coinflip(useropt, coin))
