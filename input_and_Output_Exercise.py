# Exercise 1: Accept numbers from a user
# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Exercise 3: Convert Decimal number to octal using print() output formatting
# Exercise 4: Display float number with 2 decimal places using
# Exercise 5: Accept a list of 5 float numbers as an input from the user
# Exercise 6: Write all content of a given file into a new file by skipping line number 5
# Exercise 7: Accept any three string from one input() call
# Exercise 8: Format variables using a string.format() method.
# Exercise 9: Check file is empty or not
# Exercise 10: Read line number 4 from the following file

# Exercise 1: Accept numbers from a user

# user1 = int(input("Enter Integer Number 1: "))
# user2 = int(input("Enter Integer Number 2: "))

# multi = user1 * user2
# print(multi)

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”

# print('My', 'Name', 'Is', 'James', sep='**')


# Exercise 3: Convert Decimal number to octal using print() output formatting

# user_input_number = int(input("Enter Number: "))
# convart_octal_number = oct(user_input_number)


# print(f"The octal equeblent of {user_input_number} is {convart_octal_number}")

# only user print function

# a = 8
# print(f"{oct(a)}")


# Exercise 4: Display float number with 2 decimal places using
# float_number = 12.889778
# print(f"{float_number:.2f}")


# Exercise 5: Accept a list of 5 float numbers as an input from the user

# float_number = []
# for i in range(5):
#     user_input = float(input(f"Enter Float number {i+1}: "))
#     float_number.append(user_input)

# print("Enter float number", float_number)



# Exercise 6: Write all content of a given file into a new file by skipping line number 5

# input_file_name = "test.txt"
# output_file_name = "output.txt"

# with open(input_file_name, "r") as input_file:
#     lines = input_file.readlines()
#     lines.pop(4)

# with open(output_file_name, "w") as output_file:
#     output_file.writelines(lines)


# print(output_file)




# Exercise 7: Accept any three string from one input() call

# name1, name2, name3 = input("Enter 3 string name: ").split()

# print("Name 1", name1)
# print("Name 2", name2)
# print("Name 3", name3)

# Exercise 8: Format variables using a string.format() method.

# totalMoney = 1000
# quantity = 3
# price = 450

# print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.")


# Exercise 9: Check file is empty or not

# import os

# def is_file_empty(file_path):
#     return os.path.getsize(file_path) == 0

# file_path = "output.txt"
# if is_file_empty(file_path):
#     print(f"The file {file_path} is empty")
# else:
#     print(f"The file {file_path} is not empty")

# Exercise 10: Read line number 4 from the following file

with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])