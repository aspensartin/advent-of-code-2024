import numpy as np

with open('input.txt', 'r') as input:
    data = input.read().split('\n')
    input.close()

data = [row.split() for row in data]
data = [[int(level) for level in row] for row in data]

safe_counter = 0
inc_counter = 0
dec_counter = 0

for row in data:
    for i in range(len(row)-1):
        # increasing case
        if 1 <= row[i+1]-row[i] <= 3:
            inc_counter +=1
        # decreasing case
        elif -3 <= row[i+1]-row[i] <= -1:
            dec_counter +=1
    if inc_counter == len(row)-1:
        safe_counter +=1
    elif dec_counter == len(row)-1:
        safe_counter +=1
    inc_counter = 0
    dec_counter = 0

print(safe_counter, 'reports are safe')