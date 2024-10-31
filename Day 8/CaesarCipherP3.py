alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    def encrypt(original_text, shift_amount):
        enc = ""
        for letter in original_text:
            if letter in alphabet:
                shifted = (alphabet.index(letter) + shift_amount) % len(alphabet)
                enc += alphabet[shifted]
            else:
                enc += letter  # Add non-alphabet characters as they are

        print(f"Here is the encoded result: {enc}")

    def decrypt(dec_original_text, dec_shift_amount):
        dec = ""
        for letter in dec_original_text:
            if letter in alphabet:
                shifted_dec = (alphabet.index(letter) - dec_shift_amount) % len(alphabet)
                dec += alphabet[shifted_dec]
            else:
                dec += letter  # Add non-alphabet characters as they are

        print(f"Here is the decoded result: {dec}")

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(dec_original_text=text, dec_shift_amount=shift)

    tapos = input("Type '1' to go again or '2' to exit: ")

    if tapos == '2':
        print("Thank you!")
        break
