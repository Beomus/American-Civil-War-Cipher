"""
CONTROL MESSAGE:
Rows: 4
Cols: 5
Start POS: Bottom Left (0, len(rows))
Plain text: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Cipher text: 16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19
Key: -1 2 -3 4 (The negative signals a reversed direction
"""

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

cipherlist = list(ciphertext.split())

COLS = 4
ROWS = 5
key = '-1 2 -3 4'
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

key_list = [int(i) for i in key.split()]

for k in key_list:
    if k < 0:
        col_items = cipherlist[start:stop]
    elif k > 0:
        col_items = list(reversed(cipherlist[start:stop]))

    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(translation_matrix)
