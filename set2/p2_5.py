# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 4th, 2021
# ============================================================================

import string


def caesar_cipher(phrase: str, shift: int):

    letters = string.ascii_lowercase
    digits = string.digits

    encrypted = ''

    # TO lowercase
    phrase = phrase.lower()
    print(phrase)

    # Iterar sobre cada simbolo da frase
    for ch in phrase:

        # se for uma letra, desloca-se 'shift' espaços em letters
        if ch.isalpha():
            # índice a ser criptografado
            index = letters.find(ch)

            # novo indice, após deslocamento
            new_index = (index + shift) % len(letters)
            #print(f"ch={ch} | old_ind={index}, new_ind={new_index}")

            # nova frase criptografada
            encrypted += letters[new_index]

        # se for um número, desloca-se 'shift' espaços em digits
        elif ch.isdigit():
            # índice a ser criptografado
            index = digits.find(ch)

            # novo indice, após deslocamento
            new_index = (index + shift) % len(digits)
            #print(f"ch={ch} | old_ind={index}, new_ind={new_index}")

            # nova frase criptografada
            encrypted += digits[new_index]

        # se for outro caractere, apenas copie-o
        else:
            encrypted += ch

    return encrypted


# CASOS DE USO ========================================================================================
caesar_cipher('MaThEus_99', -1)
caesar_cipher('N1c0ll1', 1)
# caesar_cipher('abcd', 1)  # retorna 'bcde'
# caesar_cipher('ABCD', 1)  # retorna 'bcde' (converta para minúsculas primeiro)
# caesar_cipher('abcd', -3)  # retorna 'xyza'

# caesar_cipher('this is pretty neat!', 2) # retorna 'vjku ku rtgvva pgcv!'

# caesar_cipher("don't you feel like a roman emperor?",13)  # "qba'g lbh srry yvxr n ebzna rzcrebe?"
# caesar_cipher("don't you feel like a roman emperor?",2)  # "fqp'v aqw hggn nkmg c tqocp gorgtqt?"
# caesar_cipher("don't you feel like a roman emperor?",-24)  # "fqp'v aqw hggn nkmg c tqocp gorgtqt?"

# caesar_cipher("hot dogs are 5.00 here?!?",2)  # 'jqv fqiu ctg 7.22 jgtg?!?'
# caesar_cipher("97 bottles of pop on the wall...",3)  # '20 erwwohv ri srs rq wkh zdoo...'
# caesar_cipher("1 is the loneliest Number...",-7)  # '4 bl max ehgxebxlm gnfuxk...'
