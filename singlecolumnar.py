import math

def encrypt(message, keyword):
    # Create an encryption matrix based on the length of the keyword
    matrix = createEncMatrix(len(keyword), message)
    # Get the sequence of numbers corresponding to the keyword
    keywordSequence = getKeywordSequence(keyword)

    ciphertext = ""
    # Iterate through the keyword sequence
    for num in range(len(keywordSequence)):
        # Find the position of the current number in the keyword sequence
        pos = keywordSequence.index(num + 1)
        # Traverse through the matrix and append characters to ciphertext
        for row in range(len(matrix)):
            # Ensure the current row has characters at the position
            if len(matrix[row]) > pos:
                ciphertext += matrix[row][pos]
    return ciphertext


def createEncMatrix(width, message):
    r = 0
    c = 0
    matrix = [[]]
    # Iterate through the message characters
    for pos, ch in enumerate(message):
        matrix[r].append(ch)
        c += 1
        # Check if the width is reached, if so, move to the next row
        if c >= width:
            c = 0
            r += 1
            matrix.append([])
    return matrix


def getKeywordSequence(keyword):
    sequence = []
    # Iterate through each character in the keyword
    for pos, ch in enumerate(keyword):
        previousLetters = keyword[:pos]
        newNumber = 1
        # Compare current character with previous ones
        for previousPos, previousCh in enumerate(previousLetters):
            if previousCh > ch:
                sequence[previousPos] += 1
            else:
                newNumber += 1
        sequence.append(newNumber)
    return sequence


def decrypt(message, keyword):
    # Create a decryption matrix using the keyword sequence
    matrix = createDecrMatrix(getKeywordSequence(keyword), message)

    plaintext = ""
    # Flatten the matrix to retrieve the decrypted message
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            plaintext += matrix[r][c]
    return plaintext

def createDecrMatrix(keywordSequence, message):
    width = len(keywordSequence)
    height = math.ceil(len(message) / width)  # Ensure height is an integer

    # Create an empty matrix based on width, height, and message length
    matrix = createEmptyMatrix(width, height, len(message))

    pos = 0
    # Iterate through the keyword sequence
    for num in range(len(keywordSequence)):
        column = keywordSequence.index(num + 1)

        r = 0
        # Fill the matrix with characters from the message
        while (r < len(matrix)) and (len(matrix[r]) > column):
            matrix[r][column] = message[pos]
            r += 1
            pos += 1

    return matrix



def createEmptyMatrix(width, height, length):
    matrix = []
    totalAdded = 0
    # Create a matrix with specified width and height
    for r in range(height):
        matrix.append([])
        for c in range(width):
            if totalAdded >= length:
                return matrix
            matrix[r].append('')
            totalAdded += 1
    return matrix


# Testing the functions
if __name__ == "__main__":
    message = "MY NAME IS KHAN"
    keyword = "HACK"
    encrypted_text = encrypt(message, keyword)
    decrypted_text = decrypt(encrypted_text, keyword)
    print("Message:", message)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
