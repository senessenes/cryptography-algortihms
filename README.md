# Cryptography Learning Journey

This repository contains my personal progress and code implementations as I learn cryptography. I am currently following the textbook *Introduction to Cryptography with Coding Theory* by Wade Trappe and Lawrence C. Washington.

So far, I have focused on classical ciphers and the math behind them. Below is a guide to the files and functions in this repository.

## Repository Contents

### 1. `general_tools.py`

This file contains foundational math algorithms and text-processing tools used frequently in cryptography. I import this into my other cipher scripts to avoid rewriting code. It utilizes `numpy` for matrix operations.

**Constants:**
*   `english_freqs`: An array containing the standard frequencies of the 26 letters in the English language.
*   `alphabet`: A list of uppercase English letters mapped from A-Z.

**Functions:**
*   `numerate(word)`
    *   **Arguments:** `word` (string) - A text string containing uppercase letters.
    *   **Returns:** A list of integers where each letter is converted to its corresponding index (A=0, B=1, ..., Z=25).
    *   **Usage:** Used to convert plain text into a mathematical format before applying encryption formulas.

*   `denumerate(number)`
    *   **Arguments:** `number` (list of integers/floats) - A list of numbers representing letters.
    *   **Returns:** A reconstructed string of uppercase letters.
    *   **Usage:** Used to convert math results back into readable cipher or plain text.

*   `extended_eucledian(a, n)`
    *   **Arguments:** `a` (int), `n` (int) - Two integers to evaluate.
    *   **Returns:** A dictionary containing `{"gcd": value, "modular_inverse": value}`. If the GCD is not 1, the modular inverse value will be "no inverse".
    *   **Usage:** Crucial for number theory operations, specifically finding the greatest common divisor (GCD) and calculating the modular inverse.

*   `adj(A)`
    *   **Arguments:** `A` (numpy array) - A square matrix.
    *   **Returns:** The adjugate (or adjoint) matrix of `A` (the transpose of the cofactor matrix).
    *   **Usage:** Used for finding the inverse of a matrix over a modulo, which is necessary for decrypting block ciphers like the Hill cipher.

### 2. `affine.py`

This file implements the Affine Cipher, where each letter $x$ is encrypted using the mathematical function $ax + b \pmod{26}$. 

**Functions:**
*   `encrypt(plain_text, key)`
    *   **Arguments:** `plain_text` (string), `key` (tuple/list of 2 integers) - The text to encrypt, and a key in the format $(a, b)$.
    *   **Returns:** The encrypted cipher text string.
    *   **Usage:** Applies the Affine encryption. Note: The greatest common divisor of $a$ and 26 must be 1 ($\gcd(a, 26) = 1$), otherwise the encryption won't be one-to-one and cannot be decrypted.

*   `decrypt_with_key(c, key)`
    *   **Arguments:** `c` (string), `key` (tuple/list of 2 integers) - The cipher text and the known $(a, b)$ key.
    *   **Returns:** The decrypted plain text string.
    *   **Usage:** Decrypts a message when the exact key is known by using the modular inverse of $a$.

*   `decrypt_cipher_only(c)`
    *   **Arguments:** `c` (string) - The cipher text to attack.
    *   **Returns:** A list of lists, where each inner list contains `[possible_decrypted_text, a, b]`.
    *   **Usage:** A brute-force attack function. Iterates through all 312 possible valid combinations of $a$ and $b$ to guess the message.

### 3. `viegenere.py`

This file implements the Vigenère Cipher, a polyalphabetic substitution cipher, as well as functions to perform cryptanalysis.

**Functions:**
*   `encrypt(plain_text, key)`
    *   **Arguments:** `plain_text` (string), `key` (string) - The message to encrypt and the keyword.
    *   **Returns:** The encrypted cipher text string.
    *   **Usage:** Shifts letters in the plain text based on the corresponding letters of the repeating keyword.

*   `decrypt(cipher, key)`
    *   **Arguments:** `cipher` (string), `key` (string) - The encrypted message and the keyword.
    *   **Returns:** The decrypted plain text string.
    *   **Usage:** Reverses the Vigenère shift using a known keyword.

*   `determine_key_size(cipher)`
    *   **Arguments:** `cipher` (string) - The intercepted cipher text.
    *   **Returns:** A list of match counts for various potential key lengths.
    *   **Usage:** A cryptanalysis tool to find repeating patterns, helping deduce the length of the unknown keyword.

*   `total_probability(l1, l2)`
    *   **Arguments:** `l1`, `l2` (lists of floats) - Two lists of frequency probabilities.
    *   **Returns:** The sum of the products of the two lists (dot product).
    *   **Usage:** Used during frequency analysis to compare expected English letter frequencies with actual frequencies.

*   `best_key_guess(key_length, cipher)`
    *   **Arguments:** `key_length` (int), `cipher` (string) - The guessed length of the keyword and the cipher text.
    *   **Returns:** A list of characters representing the most probable keyword.
    *   **Usage:** Performs frequency analysis on slices of the cipher text to programmatically guess the most likely letters of the keyword.

### 4. `block_ciphers.py`

This file implements the Hill Cipher, a polygraphic substitution cipher based on linear algebra. It uses matrices to encrypt blocks of text simultaneously.

**Functions:**
*   `encrypt(plain_text, key)`
    *   **Arguments:** `plain_text` (string), `key` (numpy array) - The message to encrypt and an $n \times n$ encryption key matrix.
    *   **Returns:** The encrypted cipher text string.
    *   **Usage:** Groups the plain text into vectors of length $n$. If the plain text length is not a multiple of $n$, it pads the end of the text with the letter "X". It then multiplies the row vectors by the key matrix modulo 26 to generate the cipher text.

*   `decrypt(cipher, encryption_key)`
    *   **Arguments:** `cipher` (string), `encryption_key` (numpy array) - The encrypted message and the original $n \times n$ encryption key matrix.
    *   **Returns:** The decrypted plain text string.
    *   **Usage:** Decrypts the cipher text by first calculating the inverse of the encryption key matrix modulo 26. It achieves this by finding the determinant of the key matrix, calculating its modular inverse, and multiplying it by the adjugate matrix (`tools.adj()`). Finally, it multiplies the cipher row vectors by this decryption matrix modulo 26 to recover the plain text.
