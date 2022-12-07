class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        keystr = str(key)
        hashVal = 0
        for ch in str(keystr):
            hashVal += ord(ch)
        
        return hashVal % self.size


    def rehash(self,key):
        # Insert your secondary hashing function code
        keystr = str(key)
        hashVal = 0
        for ch in str(keystr):
            hashVal += ord(ch)

        return (hashVal*len(keystr) % self.size)
        pass

    def put(self,key,data):
        # Insert your code here to store key and data
        index = self.hashfunction(key)
        if self.data[index] is None:
            self.slots[index] = key
            self.data[index] = data
            return

    def get(self,key):
        # Insert your code here to get data by key
        index = self.hashfunction(key)
        return f"{self.slots[index]}: {self.data[index]}"

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'
# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H.get(52))
