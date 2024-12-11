with open('input/input4.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

input = [list(line) for line in lines]  # Grid-like input
x = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "X":
            # Horizontal
            if j + 3 < len(input[i]) and input[i][j+1] == "M" and input[i][j+2] == "A" and input[i][j+3] == "S":
                x += 1
            if j - 3 >= 0 and input[i][j-1] == "M" and input[i][j-2] == "A" and input[i][j-3] == "S":
                x += 1
            # Vertical
            if i + 3 < len(input) and input[i+1][j] == "M" and input[i+2][j] == "A" and input[i+3][j] == "S":
                x += 1
            if i - 3 >= 0 and input[i-1][j] == "M" and input[i-2][j] == "A" and input[i-3][j] == "S":
                x += 1
            # Diagonal down-right
            if i + 3 < len(input) and j + 3 < len(input[i]) and \
               input[i+1][j+1] == "M" and input[i+2][j+2] == "A" and input[i+3][j+3] == "S":
                x += 1
            # Diagonal up-left
            if i - 3 >= 0 and j - 3 >= 0 and \
               input[i-1][j-1] == "M" and input[i-2][j-2] == "A" and input[i-3][j-3] == "S":
                x += 1
            # Diagonal down-left
            if i + 3 < len(input) and j - 3 >= 0 and \
               input[i+1][j-1] == "M" and input[i+2][j-2] == "A" and input[i+3][j-3] == "S":
                x += 1
            # Diagonal up-right
            if i - 3 >= 0 and j + 3 < len(input[i]) and \
               input[i-1][j+1] == "M" and input[i-2][j+2] == "A" and input[i-3][j+3] == "S":
                x += 1

print(x)
