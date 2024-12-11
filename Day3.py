import re

with open('input/input3.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

print(lines)
pattern1 = r"mul\([0-9]+,[0-9]+\)"
pattern2 = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"

mul = []
for line in lines:
    mul.append(re.findall(pattern2, line))


# pattern1_num = r"[0-9]+"

# x = []
# for l1 in mul:
#     for l2 in l1:  
#         x.append(re.findall(pattern1_num, l2))
# data = [[int(j) for j in i] for i in x]
# result = sum([x[0] * x[1] for x in data])
# print(result)

print(mul)
flat_list = [
    x 
    for xs in mul
    for x in xs
]
print("FLAT LIST")
print(flat_list)

def remove_between_elements(lst, start, end):
    result = []
    skip = False 
    for item in lst:
        if item == start: 
            skip = True
        elif item == end and skip:  
            skip = False
        if not skip and item != start and item != end :  
            result.append(item)

    return result

result2 = remove_between_elements(flat_list, "don't()", "do()")
print("WITHOUT dont and do and anythink between")
print(result2)

pattern1_num = r"[0-9]+"

x = []
for num in result2:
    x.append(re.findall(pattern1_num, num))

print("ONLY NUMBERS ")
print(x)
data = [[int(j) for j in i] for i in x]
result = sum([x[0] * x[1] for x in data])
print(result)