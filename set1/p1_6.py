# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 3rd, 2021
# =============================================================================
p_d = 5

# Imports
from math import sqrt

# Variáveis importantes
raio = p_d / 2
lim = p_d // 2
values = [num for num in range(-lim, lim + 1)]
square = []


def is_inside_circle(point):
    """
    Verifica se a distância entre um ponto e o centro [x=0, y=0] é menor que o raio
    """
    global raio
    x, y = point
    if sqrt(x**2 + y**2) <= raio:
        return True
    else:
        return False


# Variáveis informativas
f_red = '\033[1;41m'
f_gray = '\033[1m'
rem = '\033[0;0m'
tot_cells = p_d ** 2
circle_cells = 0

# Inicializando matriz
for i in range(p_d):
    square.append([0] * p_d)

# Populando matriz
for line in square:
    for i, v in enumerate(values):
        line[i] = [v, lim]
    lim -= 1

# Verificando distâncias entre pontos
for line in square:
    for index, point in enumerate(line):
        line[index] = is_inside_circle(point)
        # print(f"p{point} -> {line[index]}")  # Teste
    circle_cells += line.count(True)


# Mostrar matriz
print("\n\nSQUARE:")
for line in square:
    for element in line:
        if element:
            print(f"{f_red}{str(element):^5}{rem}", end='')
        else:
            print(f"{f_gray}{str(element):^5}{rem}", end='')
    print()

# INFORMAÇOES GERAIS
print()
print(f"Cell in circle: {circle_cells}")
print(f"Total cell square: {tot_cells}")
print(f"Estimate of Ac/As: {circle_cells / tot_cells}")
print(f"Estimate of 'pi': {(circle_cells / tot_cells) * 4}")
print()

out = (circle_cells / tot_cells) * 4
# print(out)  # Exibir resultado