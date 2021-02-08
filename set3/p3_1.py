# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 7th, 2021
# ============================================================================


def flatten_list(_list: list):
    """Retorna uma lista nivelada, isto é, retira todo e qualquer aninhamento existente.

    Args:
        _list (list): Lista inicial que deseja nivelar.

    Returns:
        list: Lista nivelada, ou seja, sem aninhamento.
    """

    f_list = []

    for element in _list:
        if type(element) != list:
            f_list.append(element)
        else:
            f_list.extend(flatten_list(element))

    return f_list


def run_length_encode_2d(array):
    """Retornar array de tuplas com número de repetições de cada elemento em sequência. 
    Exemplo: [1, 2, 2, 3, 3] -> [(1, 1), (2, 2), (2, 3)]

    Args:
        array (list): Lista que deseja codificar em RLE.

    Returns:
        list: Lista codificada.
    """

    rle = []
    count = 1

    array = flatten_list(array)

    for k, v in enumerate(array):
        if k + 1 != len(array):
            if array[k + 1] == array[k]:
                count += 1
            else:
                rle.append((count, v))
                count = 1
        else:
            rle.append((count, v))
    return rle


# test = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]

# print(run_length_encode_2d([1, 2, 3, 4, 5, 5, 5, 5]))
# print(run_length_encode_2d([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
# print(run_length_encode_2d([1, 5, 5, [5, [[0, 2, [1, 8, 9], 10, 10]], 6], 23]))
