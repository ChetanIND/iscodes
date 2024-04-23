from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

"""Use pip install pycryptodome to install the required library."""


def encrypt_aes(data, key):
    """
    Encrypts the given data using AES encryption algorithm.

    Args:
        data (bytes): The data to be encrypted.
        key (bytes): The encryption key.

    Returns:
        bytes: The encrypted data.

    """
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted_data


def decrypt_aes(encrypted_data, key):
    """
    Decrypts AES encrypted data using the provided key.

    Args:
        encrypted_data (bytes): The encrypted data to be decrypted.
        key (bytes): The key used for decryption.

    Returns:
        bytes: The decrypted data.

    """
    iv = encrypted_data[: AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(
        cipher.decrypt(encrypted_data[AES.block_size :]), AES.block_size
    )
    return decrypted_data


# Example usage:
if __name__ == "__main__":
    key = get_random_bytes(16)  # 16 bytes key for AES-128
    data = b"Hello, AES!"
    encrypted_data = encrypt_aes(data, key)
    print("Encrypted data:", encrypted_data)
    decrypted_data = decrypt_aes(encrypted_data, key)
    print("Decrypted data:", decrypted_data.decode())
