# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 2nd, 2021
# =============================================================================

numbers = [2, 7, 3, 9, 13]
mul = 1

# Verificar se a lista está vazia
if len(numbers) == 0:
    out = None

# Iterando sobre a lista e multiplicando valores
for n in numbers:
    mul *= n

# Calcular MG
out = mul ** (1 / len(numbers))

print(out)  # Exibir resultado
