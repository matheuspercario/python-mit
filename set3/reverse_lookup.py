# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 8th, 2021
# ============================================================================

def reverse_lookup(d, v):
    """Retorna uma lista com as chaves do dicionário 'd' que apontam para um determinado valor 'v'.

    Args:
        d (dict): dicionário no qual queremos encontrar todas as chaves para o valor 'v'.
        v (any): valor pelo qual desejamos encontrar as chaves correspondentes no dicionário 'd'.

    Returns:
        list: Todas as chaves referentes ao valor 'v' presente no dicionário 'd'.
    """

    out = []
    for key, value in d.items():
        if value == v:
            out.append(key)
    return out


d = {'oi': 45, 'math': 'bonito', 8.0: 'feijão', 1: 'feijão', (4, 5): 45}
print(reverse_lookup(d, 'feijão'))
print(reverse_lookup(d, 45))
print(reverse_lookup(d, 'YUEYUH'))
