# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 8th, 2021
# ============================================================================

def binary_tree_max(tree):
    # caso base
    if len(tree['children']) == 0:
        return tree['value']

    # Passo recursivo
    else:
        res = tree['value']
        c_left = binary_tree_max(tree['children'][0])
        c_right = binary_tree_max(tree['children'][1])

        # Comparação entre subarvores
        if (c_left > res):
            res = c_left
        if (c_right > res):
            res = c_right
        return res


tree = {'value': 10,
        'children': [{'value': 55, 'children': [{'value': 6, 'children': []},
                                                {'value': 44, 'children': []}, ]},

                     {'value': 120, 'children': [{'value': 11, 'children': []},
                                                 {'value': 16, 'children': []}]}]}


# print(binary_tree_max(tree))


def tree_max(tree):
    # caso base
    if len(tree['children']) == 0:
        return tree['value']

    # Passo recursivo
    else:
        res = [tree['value']]
        for k in range(len(tree['children'])):
            res.append(tree_max(tree['children'][k]))
        return max(res)


tree_2 = {'value': 13,
          'children': [{'value': 7, 'children': []},
                       {'value': 8,
                        'children': [{'value': 99, 'children': []},
                                     {'value': 16,
                                      'children': [{'value': 77, 'children': []}]},
                                     {'value': 425, 'children': []}]}]}


print(tree_max(tree_2))
