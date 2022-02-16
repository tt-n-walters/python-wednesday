
# chr()
# Number -> Letter

# ord()
# Letter - Number

# for i in range(1, 10000):
#     print(i, chr(i))

# print(ord("h"))



# Convert a whole message to numbers
# Encoding
print("Enter message to be encoded:")
message = "Hello world!"

numbers = []
print("Encoding..")
for i in range(len(message)):
    letter = message[i]
    n = ord(letter)
    numbers.append(n)

print(numbers)



# Convert numbers to a whole message
# Decoding
numbers = [
    108, 117, 106, 118, 107, 108, 107, 32, 112, 117, 32, 104, 117, 32, 104, 117, 106, 112, 108, 117,
    97, 32, 121, 118, 116, 104, 117, 32, 106, 112, 119, 111, 108, 121,
]

for j in range(26):
    for i in range(len(numbers)):
        if not numbers[i] == 32:
            numbers[i] -= 1
            if numbers[i] < 97:
                numbers[i] += 26


    # print(numbers)

    letters = []
    # print("Decoding...")
    for i in range(len(numbers)):
        n = numbers[i]
        letter = chr(n)
        letters.append(letter)


    message = "".join(letters)
    print(j, message)