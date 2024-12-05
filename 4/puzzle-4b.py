import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

lines = data.split('\n')
chars = np.array([list(i) for i in lines])
words = []
xmas = 0

for i in range(0, len(chars[3:, 0])):
    for j in range(0, len(chars[0, 3:])):
        diag1 = chars[i,j]+chars[i+1, j+1]+chars[i+2, j+2]
        diag2 = chars[i+2,j]+chars[i+1, j+1]+chars[i, j+2]
        if diag1 == 'MAS' or diag1 == 'SAM':
            if diag2 == 'MAS' or diag2 == 'SAM':
                xmas +=1

print(xmas, 'matches for x-mas')
