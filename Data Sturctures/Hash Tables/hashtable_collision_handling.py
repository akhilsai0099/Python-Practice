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
        found = False
        for ind, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][ind] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))
            

        

    def __getitem__(self , key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                print(kv[1])
                return kv[1]






t = HashTable()
t["march 6"] = 22
t["march 17"] = 120
print(t.arr)
t["march 12"]
print(t.get_hash('akhil'))