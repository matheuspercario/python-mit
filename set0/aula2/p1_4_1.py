# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 2nd, 2021
# =============================================================================

poly = [0, 0, 1/2]  # representando 1/2 x^2
new_poly = []

for index in range(len(poly)):
    #print(f'index: {index} | value: {poly[index]}')
    if index != 0:

        # Potência do termo
        p = index

        # Calculando novo valor para adicionar a nova lista (derivada)
        new_value = p * poly[index]

        # Adicionando a nova lista (derivada)
        new_poly.append(new_value)

out = new_poly  # Atribuindo nova lista (derivada) a 'out'
print(out)  # Exibir resultado
