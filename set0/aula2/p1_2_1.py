# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 2nd, 2021
# =============================================================================

numbers = [2, 7, 3, 9, 13]
_sum = 0

# Verificar se a lista está vazia
if len(numbers) == 0:
    out = None

# Iterando sobre a lista e somando valores
for n in numbers:
    _sum += n

# Calcular MA
out = _sum / len(numbers)

print(out)  # Exibir resultado
