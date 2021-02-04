# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By  : Matheus Percário Bruder
# Created Date: February 1st, 2021
# =============================================================================

year = 2017
month = 1  # 1 = janeiro, 2 = fevereiro, ..., 12 = dezembro
day = 9

y = year
m = month
d = day


# Outros valores para algoritmo de Zeller
if m in (1, 2):
    y = y - 1
    m = m + 12

a = y % 100  # Ano do século (os últimos dois dígitos do ano),
c = y // 100  # Século em questão (dois primeiros dígitos do ano)


# Valores auxiliares
aux1 = (13*(m + 1)) // 5
aux2 = a // 4
aux3 = c // 4

w = (d + aux1 + a + aux2 + aux3 - 2*c) % 7
out = w

print(out)  # Exibir resultado
