def f(L):
    """
    L é uma lista não-vazia
    """
    try:
        M = L
        P = M[:]
        #point1#
        Lnew = L.append("")
        M = sorted(M + M)
        #point2#
    except:
        print("Nothing.")


print(f([1, 2, 3]))
