from random import *
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
otherAry = []

def ShuffleIt(nlist):
    if len(nlist) > 1:
        randomInteger = randrange(0, len(nlist))
        otherAry.append(nlist.pop(randomInteger))
        ShuffleIt(nlist)
        return otherAry

print(f"Before Shuffle: {myList}")
print(f"Shuffled: ")
print(ShuffleIt(myList))