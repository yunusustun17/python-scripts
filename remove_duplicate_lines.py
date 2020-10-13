lines = []
file = open('lines.txt', 'r')
for i in file.readlines():
    lines.append(i)
file.close()

lines = set(lines)

file = open('line.txt', 'a+')
for i in lines:
    file.write(i)
file.close()
