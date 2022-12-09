
def line_search(list, term):
    list_size = len(list)
    for i in range(list_size):
        if term == list[i]:
            return True
        elif list[i] > term:
            return False

myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
myList2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(line_search(myList, 31))
print(line_search(myList, 77))
print(line_search(myList2, "Delta"))