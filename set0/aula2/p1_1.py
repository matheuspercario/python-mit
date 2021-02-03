# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 2nd, 2021
# =============================================================================

interest_rate = 0.05
capital = 1000
amount = 0
time = 1

if interest_rate <= 0:
    # Verificar se montante é o dobro do capital
    while amount < capital * 2:
        amount = capital * ((1.0 + interest_rate) ** time)
        # print(f"time {time} | amount {amount:.2f} | capital {capital}")
        time += 1  # Adicionar ano

    out = time - 1

# taxa de juros inválida
else:
    out = "NEVER"


print(out)  # Exibir resultado
