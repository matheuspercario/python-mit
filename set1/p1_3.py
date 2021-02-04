# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 3rd, 2021
# =============================================================================

dividend = 7
divisor = 2
quocient = 0

if dividend > 0 and divisor > 0:

    while quocient * divisor < dividend:
        # print(f"{quocient} * {divisor} < {dividend}")
        quocient += 1

    # Ajustando quociente após 'while'
    quocient -= 1

    # Encontrar resto da divisão
    rest = dividend - quocient * divisor

    # Declaração final
    out = (quocient, rest)

    print(out)  # Exibir resultado
