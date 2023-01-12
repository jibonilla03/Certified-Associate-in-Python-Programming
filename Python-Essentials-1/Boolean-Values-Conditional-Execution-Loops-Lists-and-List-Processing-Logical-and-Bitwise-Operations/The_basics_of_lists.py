hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1
user_number = int(input("Enter a number, to replace on the list "))
hat_list[2]=user_number

# Step 2
del hat_list[-1]

# Step 3
print(len(hat_list))