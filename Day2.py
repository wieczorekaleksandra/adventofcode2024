with open('test2.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

lines1 = []
for line in lines: 
    x = line.split()
    for i in range(0, len(x)):
        x[i] = int(x[i])
    lines1.append(x)


def function2(lines):
    i = 0
    for line in lines: 
        if all(a < b for a,b in zip(line, line[1:])) or all(a > b for a,b in zip(line, line[1:])):
           if all(abs(a - b) < 4 for a,b in zip(line,line[1:])):
            print(line)
            i = i + 1
    return i

def function3(lines):
    i = 0
    for line in lines: 
        i = i + 1
    return i


print(function3(lines1))
