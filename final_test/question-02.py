def div_by_3(x, y):
    # print(f"({x}), ({y})")
    s1 = 0
    for i in str(x):
        # print(i)
        s1 = s1 + int(i)

    s2 = 0
    for i in str(y):
        # print(i)
        s2 = s2 + int(i)

    if (s1 % 3 == 0) and (s2 % 3 == 0):
        return True
    else:
        return False


def weird_checker(func, input_list):
    out = []
    for k, v in enumerate(input_list):
        if k == len(input_list) - 1:
            break
        x = input_list[k]
        y = input_list[k + 1]
        if func(x, y):
            out.append((x, y))
    return out


# print(div_by_3(15, 12))
# nums = weird_checker(div_by_3, [1, 2, 3, 6, 9, 10, 12, 15])
# print(nums)

f = lambda x, y: x % 4 <= y % 3

input_lst = [38, -17, 71, 95, -31, 
-34, -11, -26, -49, 93, -40, 
-66, -17, -94, -92, 27, 18, 
79, 37, 63, -26, 92, 7, -89, 87
]

out = weird_checker(f, input_lst)
print(out[4])