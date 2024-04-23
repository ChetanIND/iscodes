import random


def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """
    Calculate the modular inverse of a modulo m using the extended Euclidean algorithm.
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(bits):
    """
    Generate a random prime number of specified bits length.
    """
    while True:
        prime_candidate = random.getrandbits(bits)
        if is_prime(prime_candidate):
            return prime_candidate


def generate_keypair(bits):
    """
    Generate a key pair for RSA encryption.
    """
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(message, public_key):
    """
    Encrypt a message using RSA encryption with a public key.
    """
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key):
    """
    Decrypt an encrypted message using RSA encryption with a private key.
    """
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)


# Example usage:
message = "Hello, RSA!"
public_key, private_key = generate_keypair(16)
print("Public Key:", public_key)
print("Private Key:", private_key)
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
