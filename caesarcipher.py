def caesar_encrypt(plaintext, shift):
    """Encrypt plaintext using Caesar Cipher"""
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97) # Encrypt lowercase letters
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65) # Encrypt uppercase letters
        else:
            encrypted_text += char # Leave non-alphabetic characters unchanged
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    """Decrypt ciphertext using Caesar Cipher"""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97) # Decrypt lowercase letters
            else:
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65) # Decrypt uppercase letters
        else:
            decrypted_text += char # Leave non-alphabetic characters unchanged
    return decrypted_text

# Example usage:
if __name__ == "__main__":
    plaintext = input("Enter your message to be encrypted: ")
    shift = int(input("Enter your encryption shift key: ")) # Convert input to integer

    encrypted_text = caesar_encrypt(plaintext, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("Plaintext:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
