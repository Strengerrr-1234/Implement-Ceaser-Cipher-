def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            char_code = ord(char) - ascii_offset
            if direction == "encrypt":
                char_code = (char_code + shift) % 26
            elif direction == "decrypt":
                char_code = (char_code - shift) % 26
            result += chr(char_code + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter a message to encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_message = caesar_cipher(message, shift, "encrypt")
            print(f"Encrypted message: {encrypted_message}")
        elif choice == "2":
            message = input("Enter a message to decrypt: ")
            shift = int(input("Enter a shift value: "))
            decrypted_message = caesar_cipher(message, shift, "decrypt")
            print(f"Decrypted message: {decrypted_message}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()