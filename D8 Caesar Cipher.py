alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower().strip()
shift = int(input("Enter the key:\n"))


def encrypt(original_text, shift_amount):
    newcode = []
    for j in range(len(original_text)):
        if original_text[j] in alphabet:
            for i in range(26):
                if original_text[j] == alphabet[i]:
                    newcode.append(alphabet[(i + shift_amount) % 26])
                    break
        else:
            newcode.append(original_text[j])

    print("".join(newcode))


# .............................................
# CHATGPT SUGGESTION
# can use this instead of the nested loops to work faster
#
# if char in alphabet:
#     i = alphabet.index(char)
#     newcode.append(alphabet[(i + shift) % 26])
# .............................................


def decrypt(original_text, shift_amount):
    newcode = []
    for j in range(len(original_text)):
        if original_text[j] in alphabet:
            for i in range(26):
                if original_text[j] == alphabet[i]:
                    newcode.append(alphabet[(i - shift_amount) % 26])
                    break
        else:
            newcode.append(original_text[j])

    print("".join(newcode))


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid input")
    exit(1)
