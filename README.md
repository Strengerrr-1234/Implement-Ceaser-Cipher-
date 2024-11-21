# Implement-Ceaser-Cipher
Python Program that can encrypt and decrypt text using the ceaser cipher algorithm. Allow users to input a mesaage and a shift value to perform encryption and decryption.
### 1. Function: `ceasar_cipher`

This is the core logic for the Caesar Cipher, handling both encryption
and decryption.

* Parameters:
    * `text`: The input text to encrypt or decrypt.
    * `shift`: The number of positions each letter is shifted in the
alphabet.
    * `direction`: Specifies whether to "encrypt" or "decrypt"
the message.

* Key Steps: 
### 1. Check if characters Alphabetic:
 Non-alphabetic characters (e.g., spaces, punctuation) are directly appended to the result without modification. 
### 2. Handle Upper and Lowercase Letters:
* Use 65 ('A') as the ASCII offset for uppercase letters. 
* Use 97 ('a') for
lowercase letters. 

### 3. Perform Shift Calculation: 
* For encryption: Add the
shift and take the modulo 26 to wrap around the alphabet. 
* For decryption: Subtract the shift and take the modulo 26. 

### 4. Reconstruct the New Character: 
* Convert the modified character code back to a character
using `chr`.

# 2. Function: `main`
This is the program's user interface, where users interact with the
Caesar Cipher.
* Features: 
    * Displays a menu with three options: 
      ### 1. Encrypt: 
        Prompts the user to input a message and shift value, then encrypts the message.
      ### 2. Decrypt: 
        Prompts for a message and shift value, then decrypts the
        message. 
      ### 3. Quit:
        Exits the program. Validates user choices to ensure they
        select a valid menu option.

# 3. Menu-driven Design

The program repeatedly shows the menu until the user selects "Quit".This allows users to encrypt or decrypt multiple messages without
restarting the program. 

# 4.How the Program Works

### Encryption:
* Each letter in the message is shifted forward in the alphabet by the specified shift value.
* For example, if the shift is 3, A becomes D, B becomes E, and so on. At the end of the alphabet, the shift wraps around (e.g., Z becomes C).

### Decryption:
* Each letter is shifted backward in the alphabet by the specified shift value to reverse the encryption process.

### Preservation of Non-alphabetic Characters:
* Non-alphabetic characters (e.g., spaces, numbers, punctuation) remain unchanged.

# 5. How to Build the Program

1. Set Up the Environment: Install Python on your system if it isn't
already installed. Use any Python code editor or IDE (e.g., VS Code,
PyCharm, IDLE).

2. Write the Code: Copy the provided code into a new `.py` file (e.g.,
`caesar_cipher.py`).

3. Test the Program: Run the script in the terminal or the IDE. Try
encrypting and decrypting a variety of messages to ensure correctness.

# 6. How to Execute the Program

1. Run the Program:

    * In the terminal or command prompt, navigate to the folder containing the file.

    * Run the program using the command:
```
 python caesar_cipher.py.
```

2. Interact with the Menu:

### Option 1:
Enter a message to encrypt and specify the shift value. The
program will output the encrypted message. 

### Option 2: 
Enter an encrypted message and the same shift value. The program will output the original
message. 

### Option 3:
Quit the program.

# Example of Execution

* Input and Output Example:
```
Caesar Cipher Program
1. Encrypt
2. Decrypt
3. Quit
Choose an option: 1
Enter a message to encrypt: Hello, World!
Enter a shift value: 3
Encrypted message: Khoor, Zruog!

Caesar Cipher Program
1. Encrypt
2. Decrypt
3. Quit
Choose an option: 2
Enter a message to decrypt: Khoor, Zruog!
Enter a shift value: 3
Decrypted message: Hello, World!

```
