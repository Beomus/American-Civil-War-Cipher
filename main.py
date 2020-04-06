import sys

# String to be decrypted
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# Number of cols and rows:
COLS = 4
ROWS = 5

# Key: negative means reading up, positive means reading down
key = [-1, 2, -3, 4]


def main():
    print(f"Ciphertext = {ciphertext}.")
    print(f"Trying {COLS} columns.")
    print(f"Trying {ROWS} rows.")
    print(f"Trying key {' '.join([str(i) for i in key])}.")

    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    translation_matrix = build_matrix(key, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f"Plaintext: {plaintext}.")


def validate_col_row(cipherlist):
    """Check that input columns and rows are valid against the message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)

    print(f"Length of cipher: {len_cipher}")
    print(f"Acceptable column/row values include: {factors}")
    print()

    if ROWS * COLS != len_cipher:
        print("Invalid inputs. Terminating program")
        sys.exit(1)


def build_matrix(key, cipherlist):
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key:
        if k < 0:
            col_items = cipherlist[start:stop]
        elif k > 0:
            col_items = list(reversed(cipherlist[start:stop]))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix):
    plaintext = ''
    for i in range(ROWS):
        for col in translation_matrix:
            word = str(col.pop())
            plaintext += " " + word
    return plaintext.strip()


if __name__ == "__main__":
    main()
