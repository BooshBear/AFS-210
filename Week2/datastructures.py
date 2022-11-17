Data1 = (7, False, "Apple", True, 7, 98.6)

Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

Data3 = ["A", 7, -1, 3.14, True, 7]

Data4 =  {"name": "Joe",  "age":26,   "active":True,  "hourly_wage":14.75}

print("___DATA1___")
print(len(Data1))
print(Data1[3])
print(Data1.count(7))

print("___DATA2___")
Data2.pop()
Data2.add("Alpha")
print(Data2)

print("___DATA3___")
Data3.reverse()
Data3[1] = "B"
Data3.pop()
print(Data3)

print("___DATA4___")
Data4["active"] = False
Data4.update({"address": "123 West Main Street"})
print(Data4["hourly_wage"] * 40)
print(Data4)