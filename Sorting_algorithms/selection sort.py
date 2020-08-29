def selection_sort(list):
    for i in range(0,len(list)-1):
        min_position = i
        for j in range(i+1, len(list)):
            if  list[j] < list[min_position]:
                min_position = j
        if min_position != i:

            list[i], list[min_position] = list[min_position], list[i]
    return list

# print(selection_sort([1,53,32,64,23,33]))



if __name__ == "__main__":
    nums = input("Enter your numbers using a space : ")
    nums = nums.split(" ")
    liss = []
    for num in nums:
        liss.append(int(num))
    nums = liss
    print(selection_sort(nums))