odd = filter(lambda x : x%2 != 0,range(0,int(input("enter the maximum number required : "))+1))

print(f"odd numbers are {[i for i in odd]}")