# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 8th, 2021
# ============================================================================


def lend_money(debts, person, amount):
    debts[person] = debts.get(person, []) + [amount]


def amount_owed_by(debts, person):
    return sum(debts.get(person, []))


def total_amount_owed(debts):
    tot = 0
    for value in debts.values():
        tot += sum(value)

    return tot


# Dividas
debt_dict = {
    'Joe': [5, 7],
    'Denny': [20],
    'Nicolli': [10, 20, 3, 5],
    'John': [3, 8],
    'Nick': [14],
    'Stevan': [21, 3]
}

# print(debt_dict)
# lend_money(debt_dict, 'Nicolli', 2)
# lend_money(debt_dict, 'Matheus', 14)
# print(amount_owed_by(debt_dict, 'Nicolli'))
# print(amount_owed_by(debt_dict, 'Matheus'))
# print(total_amount_owed(debt_dict))
# print(debt_dict)
