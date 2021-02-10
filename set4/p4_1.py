# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 9th, 2021
# ============================================================================

# PART 01 --------------------------------------------------------------------
# ----------------------------------------------------------------------------
def warehouse_process(dic: dict, trans: tuple):
    op, key, amount = trans

    if op == 'receive':
        dic[key] = dic.get(key, 0) + amount
    else:
        if dic.get(key, 0) < amount:
            dic[key] = 0
            print('not enough')
        else:
            dic[key] = dic.get(key, 0) - amount


# d1 = {'a': 10, 'b': 20, 'c': 30}

# Casos teste
# t1 = ('receive', 'a', 5)
# t1_1 = ('receive', 'z', 2.5)
# t2 = ('ship', 'a', 15)
# t3 = ('ship', 'c', 31)

# warehouse_process(d1, t1)  # receber
# warehouse_process(d1, t1_1)  # receber novo elemento
# warehouse_process(d1, t2)  # retirar
# warehouse_process(d1, t3)  # retirar mais que estoque
# print(d1)

# ----------------------------------------------------------------------------


# PART 02 --------------------------------------------------------------------
# ----------------------------------------------------------------------------


class Warehouse:

    def __init__(self):
        self.dict = {}

    def process(self, transaction):
        op, key, amount = transaction

        if op == 'receive':
            self.dict[key] = self.dict.get(key, 0) + amount
        else:
            if self.dict.get(key, 0) < amount:
                self.dict[key] = 0
                print('not enough')
            else:
                self.dict[key] = self.dict.get(key, 0) - amount

    def lookup(self, item):
        return self.dict.get(item, 0)


# w = Warehouse()
# w.process(('receive', 'a', 10))
# w.process(('ship', 'a', 7))
# print(w.lookup('a'))  # imprime 3
# print(w.lookup('b'))  # imprime 0
# w.process(('receive', 'b', 15))
# w.process(('receive', 'c', 7))
# w.process(('ship', 'c', 8))

# ----------------------------------------------------------------------------
