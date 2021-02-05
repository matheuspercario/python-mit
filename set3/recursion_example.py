def countdown(n: int):
    """Faz uma contagem regressiva usando recursão;

    Args:
        n (int): Contagem regressiva de 'n' até 1.
    """
    if n <= 0:
        print(f"Blastoff!")
    else:
        print(n)
        countdown(n - 1)


# countdown(5)
# countdown(-1)
# countdown(3)


def print_n(s: str, n: int):
    """Exibe na tela 'n' vezes a string 's'.

    Args:
        s (str): String fornecida pelo usuário.
        n (int): Número de vezes que string será exibida.
    """
    if n <= 0:
        return  # nota: se não dermos um valor para a instrução return, a função retorna None
    else:
        print(s)
        print_n(s, n - 1)


# print_n('Matheus', 6)
# print_n('Oi590@.', 2)
# print_n('Este é um teste! :D', -1)  # Não acontece nada devido a condição.


def fib(n: int):
    """Calcula o fibonacci relativo a 'n'.

    Args:
        n (int): Número fornecido para o qual deseja calcular o fibonacci relativo.

    Returns:
        int: Número da sequência de fibonacci relativo a 'n'.
    """
    if n < 2:  # Se n == 0 or n == 1
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(f"fib(3): {fib(3)}")
# print(f"fib(-1): {fib(-1)}")
# print(f"fib(20): {fib(20)}")


def factorial(n: int):
    """Calcular fatorial recursivamente.

    Args:
        n (int): Número que queremos encontrar o fatorial.

    Returns:
        int: Calculo do fatorial de 'n'.
    """
    if n <= 2:
        return n
    else:
        print(f"n: {n}")
        return n * factorial(n - 1)


# print(f"factorial(3): {factorial(3)}")
# print(f"factorial(5): {factorial(5)}")
# print(f"factorial(7): {factorial(-7)}")


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


# print(flatten_list([1, 2, 3]))
# print(flatten_list([1, 2, [5, [6, 7, [[0]]], 4]]))
# print(flatten_list([1, 2, [5, [6, [7, [8, 5, 6, [8]]], [[0]]], 4]]))
