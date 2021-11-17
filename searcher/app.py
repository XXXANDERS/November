filename = input('\n')
string_for_find = input('Введите строку\n')

with open(filename, 'r') as f:
    i = 0
    str_ = True
    while str_:
        str_ = f.readline()
        i += 1
        if str_.find(string_for_find) != -1:
            print(f'string #{i}: ', str_)

print('END')
