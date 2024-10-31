alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode', to encrypt, the 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))



def encrypt(original_text, shift_amount):
    ciph = ""
    for letter in original_text:
        shifted = alphabet.index(letter) + shift_amount
        shifted %= len(alphabet)
        ciph += alphabet[shifted]

    print(f"Here is the encoded result: {ciph}")
    
encrypt(original_text = text, shift_amount = shift)