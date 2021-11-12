from histogram.parser_v2 import SymbolParser

# string = input()
string = "adwnojpqwf0 -i9u08w 32r02=23ro @!@!e3-123=$%^&*()_@!#r4 .32r 9i-ri"

print('#without selected')
sp2 = SymbolParser(string)
sp2.get_count()
sp2.get_histogram()
print(sp2.sym_dict, '\n')

print('#without selected')
sp1 = SymbolParser(string, selected='a90. ')
sp1.get_count(is_select=True)
sp1.get_histogram()
print(sp1.sym_dict)
