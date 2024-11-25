signal_path = r'E:\PythonExp\Olimpiada\resources\No3\signal.txt'
decoded_path = r'E:\PythonExp\Olimpiada\resources\No3\decoded.txt'


with open(signal_path, 'r') as file:
    s = file.readline()


# A - Z (65, 91)
# a - z (97, 123)


word = []

for x in s:
    x = ord(x)
    if x in range(68, 91) or x in range(100, 123):
        word.append(chr(x-3))

    elif x in range(65, 68):
        x = 91 - (65-(x-3))
        word.append(chr(x))

    elif x in range(97, 100):
        x = 123 - (97-(x-3))
        word.append(chr(x))
    else:
        word.append(chr(x))

with open(decoded_path, 'w') as fl:
    fl.write(''.join(word))





