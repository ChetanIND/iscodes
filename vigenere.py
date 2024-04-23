# Write a program for Vigenere Cipher in Python
# Key Generation Logic
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

# Encryption Text Logic
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        cipher_text.append(chr(x + 65))
    
    return "".join(cipher_text)

# Decryption Text Logic
def originalText(string, key):
    plain_text = []
    for i in range(len(string)):
        x = (ord(string[i]) - ord(key[i])) % 26
        plain_text.append(chr(x + 65))
    
    return "".join(plain_text)

# Driver Code
if __name__ == "__main__":
    string = input("Enter your message to be encrypted: ")
    key = input("Enter your encryption key: ")
    new_key =  generateKey(string, key)
    print("\nGenerated Key is : ",new_key)
    ciphered_message = cipherText(string, new_key)
    print(f"Cipher Text: {ciphered_message}")
    print(f"Original Text: {originalText(string=ciphered_message, key=new_key)}")
