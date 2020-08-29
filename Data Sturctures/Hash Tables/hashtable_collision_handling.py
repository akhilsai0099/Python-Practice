class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for arr in range(self.Max)]

    def get_hash(self , key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self , key , value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self , key):
        h = self.get_hash(key)
        return self.arr[h]






t = HashTable()
t["march 17"] = 120
print(t.arr)
print(t["march 17"])