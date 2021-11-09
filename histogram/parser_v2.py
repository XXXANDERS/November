class SymbolParser:

    def __init__(self, string: str = "", exceptions: str = "-_!@#$*=1234567890: .?,…()&^%", selected: str = ""):
        self.str = string
        self.sym_dict = {}
        self.exceptions = exceptions
        self.selected = selected

    def get_count(self, is_select: bool = False):
        sym_dict = {}
        if is_select:
            self.str = (x.lower() for x in self.str if x in self.selected)
        else:
            self.str = (x.lower() for x in self.str if x not in self.exceptions)

        for s in self.str:
            not_empty = sym_dict.get(s)
            if not_empty is None:
                sym_dict[s] = 1
            else:
                sym_dict[s] += 1

        self.sym_dict = sym_dict
        return self.sym_dict

    def get_histogram(self):
        summ = sum((x for x in self.sym_dict.values()))
        sorted_dict = {}
        sorted_keys = sorted(self.sym_dict, key=self.sym_dict.get)
        for w in sorted_keys:
            sorted_dict[w] = self.sym_dict[w]

        for i, count in sorted_dict.items().__reversed__():
            print(f'{i} - {str((count / summ) * 100)} %')
