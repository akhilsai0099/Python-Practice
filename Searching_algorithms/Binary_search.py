def selection_sort(list):
    for i in range(0,len(list)-1):
        min_position = i
        for j in range(i+1, len(list)):
            if  list[j] < list[min_position]:
                min_position = j
        if min_position != i:

            list[i], list[min_position] = list[min_position], list[i]
    return list






pos = -1

def BinarySearch(list, value):
    lower_bound = 0
    higher_bound = len(list)-1

    while lower_bound <= higher_bound:
        mid = (lower_bound + higher_bound) //2
        if list[mid] == value:
            globals() ['pos'] = mid + 1
            return True
        else:
            if list[mid] < value:
                lower_bound = mid +1
            else:
                higher_bound = mid -1
    return False    



nums = input("Enter your numbers using a space : ")
nums = nums.split(" ")
liss = []
for num in nums:
    liss.append(int(num))
nums = liss

listed = selection_sort(nums)
print()
print(listed)
print()
value = int(input("Enter your number to check in the list : "))
print()


if BinarySearch(nums,value):
    print(f"the value has been found at position {pos}")
else:
    print("the number is not in the list of the given numbers")

input("The End") 
