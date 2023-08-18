def encrypt(text, key):
    encrypted_value = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_value += chr(((ord(char) - 97 + key) % 26) + 97)
            else:
                encrypted_value += chr(((ord(char) - 65 + key) % 26) + 65)
        else:
            encrypted_value += char    
    return encrypted_value

def decrypt(encrypted_text, key):
    decrypted_value = ''
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                    decrypted_value += chr(((ord(char) - 97 - key) % 26) + 97)
            else:
                decrypted_value += chr(((ord(char) - 65 - key) % 26) + 65)
        else:
            decrypted_value += char 
    return decrypted_value

def main():
    input_text = input("Enter the text: ")
    encryption_key = int(input("Enter the value for the key: "))

    encrypted_text = encrypt(input_text, encryption_key)
    print(encrypted_text, "encrypted")

    decrypted_text = decrypt(encrypted_text, encryption_key)
    print(decrypted_text, "decrypted")

if __name__ == "__main__":
    main()
