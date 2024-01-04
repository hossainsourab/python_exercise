'''
https://pynative.com/python-basic-exercise-for-beginners/

Exercise 1: Calculate the multiplication and sum of two number
Exercise 2: Print the sum of the current number and the previous number
Exercise 3: Print characters from a string that are present at an even index number
Exercise 4: Remove first n characters from a string
Exercise 5: Check if the first and last number of a list is the same
Exercise 6: Display numbers divisible by 5 from a list
Exercise 9: Check Palindrome Number
Exercise 10: Create a new list from two list using the following condition
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
Exercise 12: Calculate income tax for the given income by adhering to the rules below
Exercise 13: Print multiplication table from 1 to 10
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)


# Calculate the multiplication and sum of two number

def calculate_product_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2

# Example usage:
num1 = 30
num2 = 40

result = calculate_product_or_sum(num1, num2)
print("Result:", result)

'''

# Exercise 2: Print the sum of the current number and the previous number

# previous_num = 0

# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)






# for i in range(1, 11):
#     current_number = i
#     previous_number = i - 1

#     if i == 1:
#         # No previous number for the first iteration
#         print(f"For {current_number}: No previous number")
#     else:
#         sum_of_numbers = current_number + previous_number
#         print(f"For {current_number}: Sum with previous number {previous_number} is {sum_of_numbers}")

# for i in range(1, 20):
#     current_number = i
#     previous_number = i - 1

#     if i == 1:
#         # No previous number for the first iteration
#         print(f"For {current_number}: No previous number")
#     else:
#         sum_of_numbers = current_number + previous_number
#         print(f"For {current_number}: Sum with previous number {previous_number} + {current_number} is = {sum_of_numbers}")


# Exercise 3: Print characters from a string that are present at an even index number



# user_input = input("Enter your string: ")

# print("Characters at even index number")

# for i in range(0, len(user_input), 2):
#     print(user_input[i])


# Exercise 4: Remove first n characters from a string

# def wordRemover(word, n):
#     x = word[n:]
#     return x

# function_calling = wordRemover("Hello world", 3)

# print(function_calling)

# Exercise 5: Check if the first and last number of a list is the same

# def fris_and_last_chqr(list):
#     first_number = list[0]
#     last_number = list[-1]

#     if first_number == last_number:
#         return True
#     return False

# a = [12, 13,23, 12]
# b = [1,2,3,4,55,6]

# print(fris_and_last_chqr(b))

# l = [10,15,23,30]

# divisor = 5
# result = [x % divisor == 0 for x in l]
# print(result)

# for i in l:
#     if i % 5 == 0:
#         print(i)

# def disply_div_by_five(numbers):
#     divide = [num for num in numbers if num%5==0]
#     for num in divide:
#         print(num)

# number = [10,15,23,30]
# print(disply_div_by_five(number))


# Exercise 9: Check Palindrome Number



# while True:
#     user_input = str(input("Enter Number: "))
#     if user_input == "Exit":
#         break
#     else:    
#         reverse = user_input[::-1]
#         if user_input == reverse:
#             print(f"{user_input} This is Palindrome ")
#         else:
# #             print(f"{user_input} This is Not Palindrome ")


# while True:
#     user_input = input("Enter a number or type 'Exit' to quit: ")

#     if user_input.lower() == "exit":
#         break
    
#     try:
#         num = int(user_input)
#     except ValueError:
#         print("Please enter a valid number or 'Exit'.")
#         continue

#     # Convert the number to a string for easy reversal
#     num_str = str(num)

#     # Check if the reversed string is the same as the original string
#     if num_str == num_str[::-1]:
#         print(f"{num} is a palindrome number.")
#     else:
#         print(f"{num} is not a palindrome number.")



# Exercise 10: Create a new list from two list using the following

# def append_list(list1, list2):
#     result_list = []


#     for num in list1:
#         if num %2 !=0:
#             result_list.append(num)

#     for num in list2:
#         if num %2 ==0:
#             result_list.append(num)

#     return result_list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# print(append_list(list1, list2))
   

# def create_new_list(list1, list2):
#     # Filter odd numbers from list1
#     odd_numbers = [num for num in list1 if num % 2 != 0]
    
#     # Filter even numbers from list2
#     even_numbers = [num for num in list2 if num % 2 == 0]
    
#     # Concatenate the two filtered lists
#     new_list = odd_numbers + even_numbers
    
#     return new_list

# # Given lists
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# # Create the new list
# result_list = create_new_list(list1, list2)

# # Print the result
# print("Original List 1:", list1)
# print("Original List 2:", list2)
# print("New List:", result_list)


# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# exmple_number = str(input("Enter number: "))



# reverse_number = exmple_number[::-1]

# print(reverse_number, end=" ")



# Exercise 12: Calculate income tax for the given income by adhering to the rules below

# def calculate_income_tax(income):
#     if income <= 10000:
#         tax = 0
#     elif income <= 20000:
#         tax = (income - 10000) * .10
#     else:
#         tax = 10000 * .10 + (income - 20000) * .20 

#     return tax

# income_chack = calculate_income_tax(30000)
# print(income_chack)
    

# Exercise 13: Print multiplication table from 1 to 10

# for i in range(1,10):
#     for j in range(1, 10 ):
#         print(i * j, end=" ")
#     print("\t\t")


# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# for i in range(6, 0, -1):
#     for j in range(0, i):
#         print("*", end= "-")
#     print("#")


# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# base = input("Enter Base number: ")

def calculate_power(base, exp):
    power = base ** exp
    return(f"{base} raises to the power {exp} answer is {power}")

calclute = calculate_power(5, 4)
print(calclute)