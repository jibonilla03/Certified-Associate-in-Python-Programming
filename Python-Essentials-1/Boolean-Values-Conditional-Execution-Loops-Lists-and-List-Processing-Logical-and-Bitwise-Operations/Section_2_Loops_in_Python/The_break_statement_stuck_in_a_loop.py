# Alternative solution
# secret_word = input("Guess the secret word ")
# while secret_word != "chupacabra":
#     secret_word = input("Guess the secret word ")
#     if secret_word == "chupacabra":
#         print("You've successfully left the loop.")
#         break

 # Optimal solution       

while True:
    secret_word = input("You're stuck in an infinite loop!\nGuess the secret word ")
    if secret_word == "chupacabra":
        break
print("You've successfully left the loop.")