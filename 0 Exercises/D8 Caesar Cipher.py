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


def Caesar_Cipher(original_text, key, dirxn):
    """
    Takes a string (message) as input along with a key and the instruction to Encode or Decode the string, and returns the Encoded or decoded string as per the 
    """
    newcode = []
    for j in range(len(original_text)):
        if original_text[j] in alphabet:
            i = alphabet.index(original_text[j])
            if dirxn == "decode":
                newcode.append(alphabet[(i - key) % 26])
            elif direction == "encode":
                newcode.append(alphabet[(i + key) % 26])
        else:
            newcode.append(original_text[j])
    print("".join(newcode))


if direction == "encode":
    Caesar_Cipher(text, shift, direction)
elif direction == "decode":
    Caesar_Cipher(text, shift, direction)
else:
    print("Invalid input")
    exit(1)
