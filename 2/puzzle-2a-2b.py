import numpy as np

with open('input.txt', 'r') as input:
    data = input.read().split('\n')
    input.close()

data = [row.split() for row in data]
data = [[int(level) for level in row] for row in data]

safe_counter = 0
damp_counter = 0

def is_safe(row):
    inc_counter = 0
    dec_counter = 0
    for i in range(len(row)-1):
        # test ascending case
        if 1 <= row[i+1]-row[i] <= 3:
            inc_counter +=1
        # test descending case
        elif -3 <= row[i+1]-row[i] <= -1:
            dec_counter +=1
    if inc_counter == len(row)-1 or dec_counter == len(row)-1:
        return True

for row in data:
    if is_safe(row) == True:
        safe_counter +=1
    # try the Problem Dampener
    else:
        damp_rows = [np.delete(row, [j], axis=0) for j in range(len(row))]
        if True in [is_safe(row) for row in damp_rows]:
            damp_counter +=1

print(safe_counter, 'reports are safe')
print(safe_counter+damp_counter, 'reports are safe using the Problem Dampener')
