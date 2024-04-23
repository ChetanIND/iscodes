def prepare_input(text):
    # Convert the text to uppercase
    text = text.upper()
    # Replace J with I (Playfair cipher combines I and J)
    text = text.replace("J", "I")
    # Remove any characters that are not in the English alphabet
    filtered_text = "".join(filter(str.isalpha, text))
    return filtered_text

def generate_key_square(key):
    key = key.upper().replace("J", "I")
    # Remove duplicate letters from the key
    key_set = []
    for letter in key:
        if letter not in key_set:
            key_set.append(letter)
    # Generate the key square
    key_square = ""
    for i in range(65, 91): # A to Z
        if chr(i) != "J":
            if chr(i) not in key_set:
                key_set.append(chr(i))
    for i in range(0, 25, 5):
        key_square += "".join(key_set[i:i+5]) + "\n"
    return key_square

def generate_pairs(text):
    # Generate letter pairs from the plaintext
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            pairs.append((text[i], 'X')) # If the last pair has only one letter, or if two consecutive letters are the same, append 'X'
            i += 1  # Increment i to move to the next character
        else:
            pairs.append((text[i], text[i + 1]))
            i += 2
    return pairs

def encrypt(text, key):
    # Prepare input and generate key square
    text = prepare_input(text)
    key_square = generate_key_square(key)
    
    # Generate letter pairs
    pairs = generate_pairs(text)
    
    # Encrypt pairs
    cipher_text = ""
    for pair in pairs:
        first_letter_row, first_letter_col = divmod(key_square.index(pair[0]), 5)
        second_letter_row, second_letter_col = divmod(key_square.index(pair[1]), 5)
        if first_letter_row == second_letter_row:
            cipher_text += key_square[first_letter_row * 5 + (first_letter_col + 1) % 5]
            cipher_text += key_square[second_letter_row * 5 + (second_letter_col + 1) % 5]
        elif first_letter_col == second_letter_col:
            cipher_text += key_square[(first_letter_row + 1) % 5 * 5 + first_letter_col]
            cipher_text += key_square[(second_letter_row + 1) % 5 * 5 + second_letter_col]
        else:
            cipher_text += key_square[first_letter_row * 5 + second_letter_col]
            cipher_text += key_square[second_letter_row * 5 + first_letter_col]
    return cipher_text

def decrypt(cipher_text, key):
    # Prepare input and generate key square
    cipher_text = cipher_text.upper().replace("J", "I")
    key_square = generate_key_square(key)
    
    # Generate letter pairs
    pairs = generate_pairs(cipher_text)
    
    # Decrypt pairs
    plain_text = ""
    for pair in pairs:
        first_letter_index = key_square.index(pair[0])
        second_letter_index = key_square.index(pair[1])
        first_letter_row, first_letter_col = divmod(first_letter_index, 5)
        second_letter_row, second_letter_col = divmod(second_letter_index, 5)
        if first_letter_row == second_letter_row:
            plain_text += key_square[first_letter_row * 5 + (first_letter_col - 1) % 5]
            plain_text += key_square[second_letter_row * 5 + (second_letter_col - 1) % 5]
        elif first_letter_col == second_letter_col:
            plain_text += key_square[(first_letter_row - 1) % 5 * 5 + first_letter_col]
            plain_text += key_square[(second_letter_row - 1) % 5 * 5 + second_letter_col]
        else:
            plain_text += key_square[first_letter_row * 5 + second_letter_col]
            plain_text += key_square[second_letter_row * 5 + first_letter_col]
    return plain_text

if __name__ == "__main__":
    plaintext = input("Enter your message to be encrypted: ")
    key = input("Enter your encryption key: ")

    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)
