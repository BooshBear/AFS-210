from random import *
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

def ShuffleIt(nlist):
    # I believe the time complexity of this algorithm would be Linear Time 
    # because it increases in time as the array increases
    for i in nlist:
        randomInteger = randrange(0, len(nlist))
        randomPlace = nlist.pop(randomInteger)
        nlist.insert(i, randomPlace)
    return nlist

print(f"Before Shuffle: {myList}")
print(f"Shuffled: ")
print(ShuffleIt(myList))
print(ShuffleIt(myList))
print(ShuffleIt(myList))
print(ShuffleIt(myList))
print(ShuffleIt(myList))
