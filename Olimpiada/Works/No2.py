import math

in_path = r'E:\PythonExp\Olimpiada\resources\No2\in.txt'
output_path = r'E:\PythonExp\Olimpiada\resources\No2\output.txt'


with open(in_path, 'r') as file:
    lines = file.readlines()
    degrees = [float(line.split('\n')[0]) for line in lines]

radians = [math.radians(x) for x in degrees]

sin_sr = sum([math.sin(x) for x in radians])/6
cos_sr = sum([math.cos(x) for x in radians])/6

answer = round((math.degrees(math.atan2(sin_sr, cos_sr))), 6)

with open(output_path, 'w') as file:
    file.write(str(answer))



