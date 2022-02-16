
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
message = input()

for i in range(len(message)):
    letter = message[i]
    print(ord(letter))




# Convert numbers to a whole message
# Decoding
numbers = 100, 110, 60, 75, 51, 92, 101, 102

for i in range(len(numbers)):
    n = numbers[i]
    print(chr(n))
