# def sum_list(numbers):
#     # Function to calculate the sum of a list
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# # Input list creation
# L = []
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#     value=(int(input(f"Enter value {i + 1}: ")))  # Convert input to integer
#     L.append(value)
# # Calculate the sum of the list
# b = sum_list(L)
# print(f"The sum of the list is: {b}")
#largest elemet in the list
# def largest_list(numbers):
#     # Ensure the list is not empty
#     # if len(numbers) == 0:
#     #     return None  # Or raise an error, depending on your preference

#     largest = numbers[0]  # Start with the first number as the largest
#     for num in numbers:  # Loop through the list
#         if num > largest:
#             largest = num  # Update largest if current number is greater
#     return largest  # Return the largest number found

# # Input list creation
# l = []

# n = int(input("Enter the number of elements: "))
# for i in range(n):
#     value = int(input(f"Enter value {i + 1}: "))
#     l.append(value)

# # Find the largest number
# largest_number = largest_list(l)
# if largest_number is not None:
#     print(f"The largest number in the list is: {largest_number}")
# else:
#     print("The list is empty.")

class Car1:
    def  __init__(self,name,model,engine_type):
        self.name=name;
        self.model=model;
        self.engine_type=engine_type;
    def drive(self):
        print(f"{self.name} is driving");

class Tesla(Car1):
        def __init__(self,name,model,engine_type,autopilot):
            super().__init__(name,model,engine_type);
            self.autopilot=autopilot;
        # def self_drive(self):
        #     print(f"{self.name} is self driving");
    
tesla1=Tesla("Tesla","Model S","Electric","Yes");
# tesla1.self_drive();
tesla1.drive();
print(tesla1.name);
print(tesla1.model);