from caesar_art import logo
from IPython.display import clear_output
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
    
# def decrypt(cipher_text, shift):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         text += new_letter
#     print(f"The decoded text is {plain_text}")


# if(direction == "encode"):
#     encrypt(text=text, shift=shift)
# elif(direction == "decode"):
#     decrypt(cipher_text=text, shift=shift)

# def Caesar(text, shift, direction):
#     any_text = ""
#     if(shift > 26):
#         shift %= 26
#     for letter in text:
#         position = alphabet.index(letter)
#         if(direction == "encode"):
#             new_position = position + shift
#             new_letter = alphabet[new_position]
#             any_text += new_letter
#         elif(direction == "decode"):
#             new_position = position - shift
#             new_letter = alphabet[new_position]
#             any_text += new_letter
#     print(f"The {direction}d text is {any_text}")
# Caesar(text=text,shift=shift, direction=direction)

is_running = True
while is_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def Caesar(text, shift, direction):
        any_text = ""
        if(shift > 26):
            shift %= 26
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                if(direction == "encode"):
                    new_position = position + shift
                    new_letter = alphabet[new_position]
                    any_text += new_letter
                elif(direction == "decode"):
                    new_position = position - shift
                    new_letter = alphabet[new_position]
                    any_text += new_letter
            else:
                any_text += char
        print(f"The {direction}d text is {any_text}")
    Caesar(text=text,shift=shift, direction=direction)
    request = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    clear_output()
    if(request == "yes"):
        is_running = True
        print(logo)
    elif(request == "no"):
        is_running = False
        print("Goodbye")
