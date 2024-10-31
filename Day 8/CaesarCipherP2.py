alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode', to encrypt, the 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(original_text, shift_amount):
    enc = ""
    for letter in original_text:
        shifted = alphabet.index(letter) + shift_amount
        shifted %= len(alphabet)
        enc += alphabet[shifted]

    print(f"Here is the encoded result: {enc}")
        

def decrypt(dec_original_text, dec_shift_amount):
    dec = ""
    for letter in dec_original_text:
        shifted_dec = alphabet.index(letter) - dec_shift_amount
        shifted_dec %= len(alphabet)
        dec += alphabet[shifted_dec]
            
    print(f"Here is the decoded result: {dec}")
        

def caesar():
    if direction == "encode":
        encrypt(original_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt(dec_original_text = text, dec_shift_amount = shift)
        


caesar()
    
