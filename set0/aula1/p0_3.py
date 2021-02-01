# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By  : Matheus Percário Bruder
# Created Date: February 1st, 2021
# =============================================================================

kwh_used = 1000

# Calculando custo por uso
if kwh_used <= 500:  # Custo menor que 500
    cost = kwh_used * 0.45
elif 500 < kwh_used and kwh_used <= 1500:  # Custo entre 501 e 1500
    amount = 500 * 0.45
    cost = amount + (kwh_used - 500) * 0.74
elif 1500 < kwh_used and kwh_used <= 2500:  # Custo entre 1501 e 2500
    amount = 500 * 0.45 + 1000 * 0.74
    cost = amount + (kwh_used - 1500) * 1.25
else:  # Custo igual ou maior a 2501
    amount = 500 * 0.45 + 1000 * 0.74 + 1000 * 1.25
    cost = amount + (kwh_used - 2500) * 2

# Adicionando taxa de 20%
total = cost * 1.2
out = total

print(out)  # Exibir resultado
