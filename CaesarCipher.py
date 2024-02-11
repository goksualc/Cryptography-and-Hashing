ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWYZ'
KEY = 3


def caesar_encrypt(plain_text):

    cipher_text = ''
    plain_text = plain_text.upper()

    for c in plain_text:
        c='E'

        index = ALPHABET.find(c)


        index = (index + KEY) % len(ALPHABET)

        cipher_text = cipher_text + ALPHABET[index]


        return cipher_text 

