# Cryptography Learning Journey

This repository contains my personal progress and code implementations as I learn cryptography. I am currently following the textbook *Introduction to Cryptography with Coding Theory* by Wade Trappe and Lawrence C. Washington.

So far, I have focused on classical ciphers and the math behind them. Below is a guide to the files and functions in this repository.

## Repository Contents

### 1. `general_tools.py`

This file contains foundational math algorithms and text-processing tools used frequently in cryptography. I import this into my other cipher scripts to avoid rewriting code.

**Constants:**
*   `english_freqs`: An array containing the standard frequencies of the 26 letters in the English language.
*   `alphabet`: A list of uppercase English letters mapped from A-Z.

**Functions:**
*   `numerate(word)`
    *   **Arguments:** `word` (string) - A text string containing uppercase letters.
    *   **Returns:** A list of integers where each letter is converted to its corresponding index (A=0, B=1, ..., Z=25).
    *   **Usage:** Used to convert plain text into a mathematical format before applying encryption formulas.

*   `denumerate(number)`
    *   **Arguments:** `number` (list of integers) - A list of numbers from 0 to 25.
    *   **Returns:** A reconstructed string of uppercase letters.
    *   **Usage:** Used to convert math results back into readable cipher or plain text.

*   `extended_eucledian(a, n)`
    *   **Arguments:** `a` (int), `n` (int) - Two integers to evaluate.
    *   **Returns:** A dictionary containing `{"gcd": value, "modular_inverse": value}`. If the GCD is not 1, the modular inverse value will be "no inverse".
    *   **Usage:** Crucial for number theory operations, specifically finding the greatest common divisor (GCD) and calculating the modular inverse needed for decrypting affine ciphers.

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
    *   **Usage:** A brute-force attack function. Since there are only 312 valid keys for the Affine Cipher in the English alphabet, this iterates through all possible valid combinations of $a$ and $b$ to guess the message.

### 3. `viegenere.py`

This file implements the Vigenère Cipher, a polyalphabetic substitution cipher, as well as functions to perform cryptanalysis and break the cipher without knowing the key. *(Note: This file contains its own local copies of `numerate` and `denumerate` for standalone use).*

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
    *   **Usage:** A cryptanalysis tool (related to the Kasiski examination/index of coincidence). It compares the cipher text against shifted versions of itself to find repeating patterns, which helps deduce the length of the unknown keyword.

*   `total_probability(l1, l2)`
    *   **Arguments:** `l1`, `l2` (lists of floats) - Two lists of frequency probabilities.
    *   **Returns:** The sum of the products of the two lists (dot product).
    *   **Usage:** A helper mathematical function used during frequency analysis to compare expected English letter frequencies with actual frequencies in the text.

*   `best_key_guess(key_length, cipher)`
    *   **Arguments:** `key_length` (int), `cipher` (string) - The guessed length of the keyword and the cipher text.
    *   **Returns:** A list of characters representing the most probable keyword.
    *   **Usage:** Performs frequency analysis on slices of the cipher text. By comparing the letter distributions of the cipher text slices against standard English frequencies (`english_freqs`), it programmatically guesses the most likely letters of the keyword.
