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


def CC(original_text, shift_amount, dirxn):
    newcode = []
    for j in range(len(original_text)):
        if original_text[j] in alphabet:
            i = alphabet.index(original_text[j])
            if dirxn == "decode":
                newcode.append(alphabet[(i - shift_amount) % 26])
            elif direction == "encode":
                newcode.append(alphabet[(i + shift_amount) % 26])
        else:
            newcode.append(original_text[j])
    print("".join(newcode))


if direction == "encode":
    CC(text, shift, direction)
elif direction == "decode":
    CC(text, shift, direction)
else:
    print("Invalid input")
    exit(1)
