import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

lines = data.split('\n')
chars = np.array([list(i) for i in lines])
words = []

for i in range(np.size(chars, 0)-3):
    for j in range(np.size(chars, 1)-3):
        words.append(chars[i,j+k]+chars[i+1,j+k]+chars[i+2,j+k]+chars[i+3,j+k] for k in range(0,3))
        words.append(chars[i+k,j]+chars[i+k,j+1]+chars[i+k,j+2]+chars[1+k,j+3] for k in range(0,3))
        words.append(chars[i,j]+chars[i+1,j+1]+chars[i+2,j+2]+chars[i+3,j+3])
        words.append(chars[i+3,j]+chars[i+2,j+1]+chars[i+1,j+2]+chars[i,j+3])
        
print(words.count('XMAS') + words.count('SAMX'))