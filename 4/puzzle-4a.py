import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

lines = data.split('\n')
chars = np.array([list(i) for i in lines])
words = []
xmas = 0

#horizontal
for i in range(0, len(chars[3:, 0])):
    for j in range(0, len(chars[0, :])):
        if chars[i,j] == 'X' and chars[i+1, j] == 'M' and chars[i+2, j] == 'A' and chars[i+3, j] == 'S':
                xmas +=1
        if chars[i,j] == 'S' and chars[i+1, j] == 'A' and chars[i+2, j] == 'M' and chars[i+3, j] == 'X':
                xmas +=1

#vertical
for i in range(0, len(chars[0:, 0])):
    for j in range(0, len(chars[0, 3:])):
        if chars[i,j] == 'X' and chars[i, j+1] == 'M' and chars[i, j+2] == 'A' and chars[i, j+3] == 'S':
            xmas +=1
        if chars[i,j] == 'S' and chars[i, j+1] == 'A' and chars[i, j+2] == 'M' and chars[i, j+3] == 'X':
            xmas +=1
        
#top-left -> bottom-right
for i in range(0, len(chars[3:, 0])):
    for j in range(0, len(chars[0, 3:])):
        if chars[i,j] == 'X' and chars[i+1, j+1] == 'M' and chars[i+2, j+2] == 'A' and chars[i+3, j+3] == 'S':
            xmas +=1
        if chars[i,j] == 'S' and chars[i+1, j+1] == 'A' and chars[i+2, j+2] == 'M' and chars[i+3, j+3] == 'X':
            xmas +=1

#top-right -> bottom-left
for i in range(3, len(chars[:, 0])):
    for j in range(0, len(chars[0, 3:])):
        if chars[i,j] == 'X' and chars[i-1, j+1] == 'M' and chars[i-2, j+2] == 'A' and chars[i-3, j+3] == 'S':
            xmas +=1
        if chars[i,j] == 'S' and chars[i-1, j+1] == 'A' and chars[i-2, j+2] == 'M' and chars[i-3, j+3] == 'X':
            xmas +=1       

print(xmas, 'matches for xmas')
