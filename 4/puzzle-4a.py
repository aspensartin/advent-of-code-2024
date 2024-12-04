import numpy as np

with open('test-input.txt', 'r') as input:
    data = input.read()
    input.close()

lines = data.split('\n')
chars = np.array([list(i) for i in lines])
words = [] 

for i in range(len(chars[:, 0])):
    for j in range(len(chars[0, :])):
        if j < len(chars[:, 0])-3:
            words.append(chars[i,j]+chars[i,j+1]+chars[i,j+2]+chars[1,j+3])
        if i < len(chars[0, :])-3:
            words.append(chars[i,j]+chars[i+1,j]+chars[i+2,j]+chars[i+3,j])
        if i < len(chars[0, :])-3 and j < len(chars[:, 0])-3: 
            words.append(chars[i,j]+chars[i+1,j+1]+chars[i+2,j+2]+chars[i+3,j+3])
        if i >= 3 and j < len(chars[0, :])-3:
            words.append(chars[i,j]+chars[i-1,j+1]+chars[i-2,j+2]+chars[i-3,j+3])

np.savetxt('words.txt', words, fmt='%s')
print(words.count('XMAS')+words.count('SAMX'))
