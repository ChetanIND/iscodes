import numpy as np

def egcd(a, b):
    """Extended Euclidean Algorithm to find the multiplicative inverse"""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    """Calculate the multiplicative inverse of 'a' modulo 'm'"""
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def matrix_mod_inverse(matrix, modulus):
    """Calculate the inverse of a matrix modulo 'modulus'"""
    det = int(np.round(np.linalg.det(matrix)))  # Calculate determinant
    det_inv = mod_inverse(det, modulus)         # Calculate determinant inverse modulo 'modulus'
    matrix_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus
    return matrix_inv

def hill_encrypt(plaintext, key):
    """Encrypt plaintext using Hill Cipher"""
    n = len(key) # Size of the key matrix
    plaintext = [ord(char) - 65 for char in plaintext] # Convert plaintext characters to numbers
    while len(plaintext) % n != 0: # Pad the plaintext with 'X' to make its length divisible by n
        plaintext.append(23) # ASCII code for 'X' - 65 = 23
    plaintext = np.array(plaintext).reshape(-1, n) # Reshape the plaintext into a matrix
    ciphertext = np.dot(plaintext, key) % 26 # Multiply plaintext matrix with key matrix and take modulo 26
    ciphertext = ''.join([chr(char + 65) for row in ciphertext for char in row]) # Convert numbers to characters
    return ciphertext

def hill_decrypt(ciphertext, key):
    """Decrypt ciphertext using Hill Cipher"""
    n = len(key) # Size of the key matrix
    key_inv = matrix_mod_inverse(key, 26) # Calculate the inverse of the key matrix modulo 26
    ciphertext = [ord(char) - 65 for char in ciphertext] # Convert ciphertext characters to numbers
    ciphertext = np.array(ciphertext).reshape(-1, n) # Reshape the ciphertext into a matrix
    plaintext = np.dot(ciphertext, key_inv) % 26 # Multiply ciphertext matrix with inverse key matrix and take modulo 26
    plaintext = ''.join([chr(char + 65) for row in plaintext for char in row]) # Convert numbers to characters
    return plaintext

if __name__ == "__main__":
    # Example usage:
    plaintext = "HELLO"
    key = np.array([[3, 2], [5, 7]]) # Example key matrix
    encrypted_text = hill_encrypt(plaintext, key)
    decrypted_text = hill_decrypt(encrypted_text, key)
    print("Plaintext:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
