def Linear_search(list,value):
    i = 0
    while i<len(list):
        if list[i] == value :
            return  f"{True} found at position {i+1}"
        i += 1
        
    return False
        
list = [1,53,32,64,23,33]

print(Linear_search([1,53,32,64,23,33],3))
