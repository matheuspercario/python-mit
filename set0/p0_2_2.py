# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By  : Matheus Percário Bruder
# Created Date: February 1st, 2021
# =============================================================================

a = 1
b = 2
c = 3

# Testar se é uma eq de 2º grau
if a == 0:
    out = - c / b

# Calcular valor de delta
delta = (b ** 2) - 4 * a * c

# Calculando raízes
x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

if delta == 0:
    out = x1
else:
    out = x1, x2

print(out)  # Exibir resultado
