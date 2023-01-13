# Optimal solution
# word_without_vowels = ""

# # Prompt the user to enter a word
# user_word = input("Enter any word: ")
# # and assign it to the user_word variable.
# user_word = user_word.upper()

# for letter in user_word:
#     if letter not in ['A','E','I','O','U']:
#         word_without_vowels += letter
     

# print(word_without_vowels)

# Alternative solution

word_without_vowels = ""

user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
		
print(word_without_vowels)

