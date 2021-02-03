# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 2nd, 2021
# =============================================================================

poly = [0, 1, 2, 6]
new_poly = []
const = 4

# Adicionando constante a lista
new_poly.append(const)

# Iterar sobre cada termo do polinomio
for index in range(len(poly)):
    #print(f'index: {index} | value: {poly[index]}')

    # Potência do termo
    p = index

    # Calculando novo valor para adicionar a nova lista
    new_value = poly[index] / (p + 1)

    # Adicionando a nova lista
    new_poly.append(new_value)

out = new_poly  # Atribuindo nova lista a 'out'
print(out)  # Exibir resultado
