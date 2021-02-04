# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By  : Matheus Percário Bruder
# Created Date: February 1st, 2021
# =============================================================================

# Equação -> http://s3-sa-east-1.amazonaws.com/descomplica-blog/wp-content/uploads/2015/08/mapamental-matematica-geometria-analitica.jpg

px = 1
py = 2
a = 3
b = 4
c = 5

# numerador
n = abs(a*px + b*py + c)

# denominador
d = (a**2 + b**2) ** (1 / 2)

# Calcular distância entre ponto e reta
out = n / d

print(out)  # Exibir resultado
