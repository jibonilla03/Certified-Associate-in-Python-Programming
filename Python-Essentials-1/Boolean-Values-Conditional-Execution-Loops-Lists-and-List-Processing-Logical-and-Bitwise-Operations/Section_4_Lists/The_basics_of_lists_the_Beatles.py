
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(0,2):
    member=input("Enter new Beatles's member name: ")
    beatles.append(member)
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]

print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

# Alternative optimal solution

# step 1:
# Beatles = []
# print("Step 1:", Beatles)

# # step 2:

# Beatles.append("John Lennon")
# Beatles.append("Paul McCartney")
# Beatles.append("George Harrison")
# print("Step 2:", Beatles)

# # step 3:
# for members in range(2):
#     Beatles.append(input("New band member: "))
# print("Step 3:", Beatles)

# # step 4:
# del Beatles[-1]
# del Beatles[-1]
# print("Step 4:", Beatles)

# # step 5:
# Beatles.insert(0, "RingoStarr")
# print("Step 5:", Beatles)
# print("The Fab:",len(Beatles))