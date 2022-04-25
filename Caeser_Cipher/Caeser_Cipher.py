# Casaer Cipher Encryption and unencryption
# uses ord() and char() as foundation for encrypting
# Encrypts and decrypts all characters (excludes DEL, and first 32 non printable characters)

# GLOBALS


SHIFT_AMOUNT = 5

def Encrypt(message):
    encrypted = ""
    for letter in message:
        new_ascii = ord(letter) + SHIFT_AMOUNT
        if new_ascii > 126:
            new_ascii = 31 + (new_ascii - 126)
        encrypted += chr(new_ascii)
    
    return encrypted


def Decrypt(message):
    decrypted = ""
    for letter in message:
        new_ascii = ord(letter) - SHIFT_AMOUNT
        if new_ascii < 32:
            new_ascii = 127 - (32 - new_ascii)
        decrypted += chr(new_ascii)

    return decrypted

if __name__ == "__main__":
    encrypted_string = Encrypt(str(input("Please Enter a string to be enrypted: ")))
    decrypted_string = Decrypt(encrypted_string)

    print(f"The encrypted message is: {encrypted_string}")
    print(f"The decrypted message is: {decrypted_string}")
