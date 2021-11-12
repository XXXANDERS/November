import sys
sys.path.append('../')  # делаем все внешние модули видемыми

from histogram.parser_v2_1 import SymbolParser

string = input()

sp1 = SymbolParser(string, selected='абвгдеёжзийклмнопрстуфхцчшщьыъэюя')
sp1.get_count(is_select=True)
# sp1.get_histogram()
sp1.get_histogram(vertical=True, down_top=True)
