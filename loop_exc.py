    # Exercise 1: Print First 10 natural numbers using while loop
    # Exercise 2: Print the following pattern
    # Exercise 3: Calculate the sum of all numbers from 1 to a given number
    # Exercise 4: Write a program to print multiplication table of a given number
    # Exercise 5: Display numbers from a list using loop
    # Exercise 6: Count the total number of digits in a number
    # Exercise 7: Print the following pattern
    # Exercise 8: Print list in reverse order using a loop
    # Exercise 9: Display numbers from -10 to -1 using for loop
    # Exercise 10: Use else block to display a message “Done” after successful execution of for loop
    # Exercise 11: Write a program to display all prime numbers within a range
    


# Exercise 1: Print First 10 natural numbers using while loop

# for i in range(1,11):
#     print(i)

# Exercise 2: Print the following pattern
    
# for i in range(1, 5+1, 1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print(" ")



# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# s = 0
# n = int(input("Enter number: "))
# for i in range(1, n+1):
#     s += i
# print(s)


# Exercise 4: Write a program to print multiplication table of a given number

# user_input = int(input("Enter number: "))
# for i in range(1, 11):
#     print(f" {user_input} * {i} = {i*user_input}")


# Exercise 5: Display numbers from a list using loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if i % 5 == 0:
#         print(i)


# Exercise 6: Count the total number of digits in a number

# Get the number from the user
# number = int(input("Enter a number: "))

# num_str = str(number)
# num_digits = len(num_str)

# print(f"The number of digits in {number} is: {num_digits}")

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()



# Exercise 8: Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]

# newlist = reversed(list1)

# for i in newlist:
#     print(i)


# Exercise 9: Display numbers from -10 to -1 using for loop

# for num in range(-10, 0, 1):
#     print(num)


# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# for i in range(5):
#     print(i)
# else:
#     print("Done!")


# Exercise 11: Write a program to display all prime numbers within a range


# user_input = int(input("Enter number: "))

# if user_input == 2:
#     print("2 is prime")

# elif user_input % 2==0:
#     print(f"{user_input} Note prime")
# else:
#     print(f"{user_input} prime")
