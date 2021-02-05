# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 4th, 2021
# ============================================================================

def largest_number(input_list):
    """Encontrar maior número da lista fornecida pelo usuário

    Args:
        input_list (list): Lista de números (floats, ints) fornecida pelo usuário.

    Returns:
        int, float: Maior número presente na lista.
    """
    if len(input_list) in (0, 1):
        return None

    best_so_far = input_list[0]

    for value in input_list:
        if value > best_so_far:
            best_so_far = value

    return best_so_far


def second_largest_number(input_list):
    """Encontrar segundo maior número da lista.

    Args:
        input_list (list): Lista de números fornecida pelo usuário.

    Returns:
        int, float: Segundo maior número da lista.
    """
    # Somente listas com dois ou mais elementos
    if len(input_list) in (0, 1):
        return None

    best_so_far = largest_number(input_list)

    # Encontrar menor número
    second_best = input_list[0]
    for value in input_list:
        if value < second_best:
            second_best = value

    # Incrementar até encontrar o segundo melhor
    for value in input_list:
        if value > second_best and value < best_so_far:
            second_best = value

    return second_best


print(largest_number([5.2, 85.6, 54.8, 6.5, 4.5]))
print(second_largest_number([]))
print(second_largest_number([2]))
print(second_largest_number([94, 87, 20, 35]))
print(second_largest_number([1, 2, 3, 3, 3]))
print(second_largest_number([20, -1, -10]))
print(second_largest_number([20.5, -1.2, -10.2356]))
