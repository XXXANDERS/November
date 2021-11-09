string = "abcdefghijklmnopqrstuvwxyz"


def counter(str_):
    sym_dict = {}
    str_ = str_.replace(' ', '')
    for s in str_:
        not_empty = sym_dict.get(s, -1)
        if not_empty != -1:
            sym_dict[s] += 1
        else:
            sym_dict[s] = 1
    return sym_dict


def histogram(sym_dict):
    summ = 0
    for _, count in sym_dict.items():
        summ += count
    for i, count in sym_dict.items():
        sym_dict[i] = str((count / summ)*100) + '%'

    for i, data in sym_dict.items():
        print(f"{i} - {data}")


histogram(counter(string))
