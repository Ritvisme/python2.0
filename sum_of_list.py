def sum_list(numbers):
    # Function to calculate the sum of a list
    total = 0
    for num in numbers:
        total += num
    return total

# Input list creation
L = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    value=(int(input(f"Enter value {i + 1}: ")))  # Convert input to integer
    L.append(value)
# Calculate the sum of the list
b = sum_list(L)
print(f"The sum of the list is: {b}")