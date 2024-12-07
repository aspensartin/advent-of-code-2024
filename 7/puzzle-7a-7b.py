import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

eqs = [[np.char.strip(i.split(' '), ':')] for i in data.split('\n')]

def add_or_mult(eqn):
    a = np.array(eqn[0]).flatten()
    b = int(eqn[1])
    if type(a) == int:
        output = [a+b, a*b]
    else:
        output = np.array([[int(i)+b, int(i)*b] for i in a]).flatten()
    if len(eqn) == 2:
        return output
    eqn[1] = output
    eqn.pop(0)
    return add_or_mult(eqn)

def add_mult_or_concat(eqn):
    a = np.array(eqn[0]).flatten()
    b = int(eqn[1])
    if type(a) == int:
        output = [a+b, a*b, int(str(a)+str(b))]
    else:
        output = np.array([[int(i)+b, int(i)*b, str(i)+str(b)] for i in a]).flatten()
    if len(eqn) == 2:
        return output
    eqn[1] = output
    eqn.pop(0)
    return add_mult_or_concat(eqn)

result_a = 0
result_b = 0

for i in eqs:
    eqn = [int(j) for j in i[0][1:]]
    ans = int(i[0][0])
    if ans in add_or_mult(eqn):
        result_a += ans
    if ans in add_mult_or_concat(eqn):
        result_b += ans

print('calibration result is', result_a, 'or', result_b, 'including concatenations')
