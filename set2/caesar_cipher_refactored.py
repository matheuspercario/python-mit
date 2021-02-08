# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 4th, 2021
# ============================================================================

import string


def encode(char, serie, shift):

    index = serie.find(char)  # indice atual
    new_index = (index + shift) % len(serie)  # novo indice, apos deslocamento

    return serie[new_index]


def caesar_cipher(phrase: str, shift: int):

    encrypted = ''

    # TO lowercase
    phrase = phrase.lower()
    print(phrase)

    for ch in phrase:

        if ch.isalpha():  # Letra
            encrypted += encode(ch, string.ascii_lowercase, shift)
        elif ch.isdigit():  # Digito
            encrypted += encode(ch, string.digits, shift)
        else:  # Pontuação
            encrypted += ch

    return encrypted


print(caesar_cipher('N1c0ll1', 1))
print(caesar_cipher("don't you feel like a roman emperor?", 1356))
