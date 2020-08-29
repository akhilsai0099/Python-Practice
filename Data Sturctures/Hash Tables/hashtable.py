class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]


    def get_hash(self , key):
        sum = 0
        for a in key:
            sum += ord(a)
        return sum % self.Max

    def __setitem__(self , key , value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self , key):
        h = self.get_hash(key)
        return self.arr[h]

    


table = HashTable()
