# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 8th, 2021
# ============================================================================

from string import ascii_lowercase, digits


def encode(char, serie, shift):
    index = serie.find(char)  # indice atual
    new_index = (index + shift) % len(serie)  # novo indice, apos deslocamento
    return serie[new_index]


def caesar_cipher(phrase: str, shift: int):
    phrase = phrase.lower()  # TO lowercase
    encrypted = ''

    for ch in phrase:
        if ch.isalpha():  # Letra
            encrypted += encode(ch, ascii_lowercase, shift)
        elif ch.isdigit():  # Digito
            encrypted += encode(ch, digits, shift)
        else:  # Pontuação
            encrypted += ch

    return encrypted


print(caesar_cipher('N1c0ll1', 1))
print(caesar_cipher("don't you feel like a roman emperor?", 1356))
