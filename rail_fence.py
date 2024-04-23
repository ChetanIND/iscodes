def encrypt_rail_fence(plaintext, key):
    # Initialize ciphertext list with empty strings
    ciphertext = [""] * len(plaintext)
    # Initialize rail list to hold characters in each rail
    rail = [""] * key
    # Initialize direction of movement along the rails
    direction = -1
    row = 0

    # Fill the rail list with characters from the plaintext
    for char in plaintext:
        rail[row] += char
        # Change direction when reaching the top or bottom rail
        if row == 0 or row == key - 1:
            direction *= -1
        # Move to the next row according to the direction
        row += direction

    # Reconstruct the ciphertext from the filled rail list
    index = 0
    for i in range(key):
        for j in range(len(rail[i])):
            ciphertext[index] = rail[i][j]
            index += 1

    return "".join(ciphertext)


def decrypt_rail_fence(ciphertext, key):
    # Initialize plaintext list with empty strings
    plaintext = [""] * len(ciphertext)
    # Initialize rail list to reconstruct characters in each rail
    rail = [""] * key
    # Initialize direction of movement along the rails
    direction = -1
    row = 0

    # Fill the rail list with placeholder characters '*'
    for char in ciphertext:
        rail[row] += "*"
        # Change direction when reaching the top or bottom rail
        if row == 0 or row == key - 1:
            direction *= -1
        # Move to the next row according to the direction
        row += direction

    # Replace placeholder characters with characters from the ciphertext
    index = 0
    for i in range(key):
        for j in range(len(rail[i])):
            rail[i] = rail[i][:j] + ciphertext[index] + rail[i][j + 1 :]
            index += 1

    # Reconstruct plaintext by reading characters from the rails
    row = 0
    direction = -1
    for i in range(len(ciphertext)):
        plaintext[i] = rail[row][0]
        rail[row] = rail[row][1:]
        # Change direction when reaching the top or bottom rail
        if row == 0 or row == key - 1:
            direction *= -1
        # Move to the next row according to the direction
        row += direction

    return "".join(plaintext)


# Example usage:
plaintext = "Hello World"
key = 3
encrypted_text = encrypt_rail_fence(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted text:", decrypted_text)
