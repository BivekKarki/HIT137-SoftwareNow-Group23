#  Group Name: SYDN 23
#  Group Members: 
#  Bivek Karki- 395860
#  Subodh Budhathoki - S394191
#  Bayezid Bin Zahid - S391465
#  Nancy Nancy - S395843

# Text Encryption/Decryption Program
# Description: This program reads text from a file, encrypts it using user-provided shift numbers, 
# writes the encrypted text to a file, then decrypts it back and verifies that the original text matches.

# encryption function to encrypt text based on user input shift number
def encrypt(text, shift1, shift2):
    result = [] # This will store the encrypted characters
    for char in text:
        if 'a' <= char <= 'm':  # lowercase a–m
            base = ord('a') # Get ASCII value of 'a'
            new_pos = (ord(char) - base + shift1) % 13 # Shift and wrap around
            result.append(chr(base + new_pos)) # It convert ASCII value back to character

        elif 'n' <= char <= 'z':  # lowercase n–z
            base = ord('n')
            new_pos = (ord(char) - base - shift1) % 13  # Shift backward
            result.append(chr(base + new_pos))

        elif 'A' <= char <= 'M':  # uppercase A–M
            base = ord('A')
            new_pos = (ord(char) - base + shift2) % 13 # Shift forward
            result.append(chr(base + new_pos))

        elif 'N' <= char <= 'Z':  # uppercase N–Z
            base = ord('N')
            shift_val = shift2 ** 2  # Shift is square of shift2
            new_pos = (ord(char) - base + shift_val) % 13
            result.append(chr(base + new_pos))

        else:
            result.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(result)

# Function to decrypt text back to original text
def decrypt(text, shift1, shift2):
    result = []
    for char in text:
        if 'a' <= char <= 'm':  # lowercase a–m
            base = ord('a')
            new_pos = (ord(char) - base - shift1) % 13
            result.append(chr(base + new_pos))

        elif 'n' <= char <= 'z':  # lowercase n–z
            base = ord('n')
            new_pos = (ord(char) - base + shift1) % 13
            result.append(chr(base + new_pos))

        elif 'A' <= char <= 'M':  # uppercase A–M
            base = ord('A')
            new_pos = (ord(char) - base - shift2) % 13
            result.append(chr(base + new_pos))

        elif 'N' <= char <= 'Z':  # uppercase N–Z
            base = ord('N')
            shift_val = shift2 ** 2
            new_pos = (ord(char) - base - shift_val) % 13
            result.append(chr(base + new_pos))

        else:
            result.append(char)
    return ''.join(result)

# Main part of the program
try:
    shift1 = int(input("Enter shift1 (integer): ")) # Ask the user for shift values
    shift2 = int(input("Enter shift2 (integer): "))

    filename = "raw_text.txt"

    # Read the text from file [raw_text.txt]
    with open(filename, "r", encoding="utf-8") as f:
        original_text = f.read()
  
    # Encrypt and write to file
    encrypted_text = encrypt(original_text, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)
    # print(encrypted_text)
    print("Encrypted -> encrypted_text.txt")
    

    # Decrypt and write to file
    decrypted_text = decrypt(encrypted_text, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)
    # print(decrypted_text)
    print("Decrypted -> decrypted_text.txt")

     # Verify if decrypted text matches original text
    if original_text == decrypted_text:
        print("Verification: SUCCESS — decrypted text matches the original text.")
    else:
        print("Verification: FAILED — decrypted text does NOT match the original text.")

# Error handling for missing file
except FileNotFoundError:
    print(f"Error: '{filename}' not found. Please create or rename the file with some text.")

# Error handling for invalid user input
except ValueError:
    print("Error: Shift values must be integers.")

# Catch any other unexpected errors
except Exception as e:
    print(f"Unexpected error: {e}")