with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

list1 = []
list2 = []
for line in lines:
    x = line.split()
    #print(x)
    list1.append(int(x[0]))
    list2.append(int(x[1]))

list1 = sorted(list1)
list2 = sorted(list2)

# TASK 1 -> list 3
# TASK 2 -> list 4
list3 = []
list4 = []
for i in range(0, len(list1)):
    list3.append(abs(list1[i] - list2[i]))
    list4.append(list1[i] * list2.count(list1[i]))

print(sum(list3))
print(sum(list4))