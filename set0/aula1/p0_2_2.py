# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By  : Matheus Percário Bruder
# Created Date: February 1st, 2021
# =============================================================================

a = 1
b = 2
c = 3

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
