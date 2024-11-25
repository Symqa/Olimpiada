import re

input_path = r'E:\PythonExp\Olimpiada\resources\No1\input.txt'

with open(input_path, 'r') as file:
    s = file.readline()


word = re.findall('.{%s}' % 8, s)
word = [int(x, 2) for x in word]

print(''.join([chr(x) for x in word]))


