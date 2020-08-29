def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list

nums = input("Enter your numbers using a space : ")
nums = nums.split(" ")
liss = []
for num in nums:
    liss.append(int(num))
nums = liss
print(sort(nums))
