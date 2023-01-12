# Alternative solution
# secret_number = 777
# picked_number = 0

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# while picked_number != secret_number:
#     picked_number = int(input("Enter your guess: "))
#     if picked_number == secret_number:
#         print(secret_number, "Well done, muggle! You are free now.")
#     else:
#         print("Ha ha! You're stuck in my loop!")

## Optimized solution
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter the number: "))

while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")