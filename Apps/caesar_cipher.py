letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n''o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt (text, shift):
    encrypted_text = ""
    for letter in text:
        shifted_letter = letter.index(letter) + shift #((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        shifted_letter %= len(letters)
        encrypted_text += letters[shifted_letter]
    return encrypted_text

def decrypt (text, shift):
    decrypted_text = ""
    for letter in text:
        shifted_letter = letter.index(letter) - shift #((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        shifted_letter %= len(letters)
        encrypted_text += letters[shifted_letter]
    return decrypted_text

# Example usage
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))
encrypted_text = encrypt(text, shift)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)