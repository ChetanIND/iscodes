from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

"""Use pip install pycryptodome to install the required library."""


def encrypt_des(data, key):
    """
    Encrypts the given data using the DES algorithm.

    Args:
        data (bytes): The data to be encrypted.
        key (bytes): The encryption key.

    Returns:
        bytes: The encrypted data.
    """
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data, DES.block_size))
    return encrypted_data


def decrypt_des(encrypted_data, key):
    """
    Decrypts the given encrypted data using the DES algorithm.

    Args:
        encrypted_data (bytes): The encrypted data to be decrypted.
        key (bytes): The key used for decryption.

    Returns:
        bytes: The decrypted data.

    Raises:
        ValueError: If the key length is invalid.

    """
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
    return decrypted_data


# Example usage:
if __name__ == "__main__":
    key = get_random_bytes(8)  # 8 bytes key for DES
    data = b"Hello, DES!"
    encrypted_data = encrypt_des(data, key)
    print("Encrypted data:", encrypted_data)
    decrypted_data = decrypt_des(encrypted_data, key)
    print("Decrypted data:", decrypted_data.decode())
