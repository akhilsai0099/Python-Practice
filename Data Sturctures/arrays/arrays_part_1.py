expenses = [2200,2350,2600,2130,2190]
# In Feb, how many dollars you spent extra compare to January?
print(f"In February you spent {expenses[1]-expenses[0]} extra compared to January")

# Find out your total expense in first quarter (first three months) of the year.
print(f"The total expence of the first quarter is {expenses[0]+expenses[1]+expenses[2]}")

# Find out if you spent exactly 2000 dollars in any month
print(f"Did i spend 2000$ in any month :- {2000 in expenses}")

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(expenses)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200

print(expenses)
