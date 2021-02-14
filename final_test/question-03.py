def make_change(amount):
    """
    Assume que amount é um inteiro > 0, em centavos
    Retorna o menor número de moedas cujos valores somam a amount.
    * Moedas possíveis são 100, 50, 25, 10, 5, 1 centavos
    * Um algoritmo ganancioso funciona aqui
    """
    out = []
    for p in 100, 50, 25, 10, 5, 1:

        if amount >= p:
            n = amount // p
            r = amount - p * n
            print(f"valor ={amount} | notas ={n} | nota ={p} | resto ={r}")
            amount = r
            out.append(n)

    print(out)
    return sum(out)


# print(make_change(256))
print(make_change(1550442))
print(make_change(329294392))
print(make_change(7777777))
print(make_change(15564))
