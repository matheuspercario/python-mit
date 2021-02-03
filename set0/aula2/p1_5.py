# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 2nd, 2021
# =============================================================================

# size = 'medium'
# toppings = ['atum', 'cebola', 'abacaxi']

size = 'small'
toppings = ['presunto', 'abacaxi']

flag = 0


# Calculando valor para diferentes tamanhos
if size == 'small':
    cost = 14
elif size == 'medium':
    cost = 16
else:
    cost = 18


# Iterar sobre coberturas incrementando valor total
for index in range(len(toppings)):
    # Verificar se é bacon ou anchovas
    if toppings[index] == 'bacon' or toppings[index] == 'anchovas':
        flag += 1

    # Percentual adicional da cobertura
    percent = (12 + index + len(toppings[index])) / 100
    # Valor da cobertura de acordo com percentual e tamanho
    top_value = cost * percent
    # Valor total até o momento
    cost += top_value
    # Visualização
    print(
        f"{toppings[index]}: ({int(percent*100)}%), ${round(top_value, 2)} || TOTAL ${round(cost, 2)}")


# Devo acrescentar adicional de bacon ou anchovas?
if flag > 0:
    cost *= 1.1


out = round(cost, 2)
print(out)  # Exibir resultado
