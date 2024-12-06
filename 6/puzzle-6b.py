import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

map = np.array([list(i) for i in data.split('\n')])
path = np.zeros_like(map, dtype='int')    
dir = np.array([-1, 0])
pos_0 = np.argwhere(map == '^').flatten()
pos = pos_0
step_count = 0
loop_count = 0

path[pos[0], pos[1]] = 1

for i in range(len(map[:, 0])):
    for j in range(len(map[0, :])):
        if map[i, j] == '#':
            print('obstruction at', i, j, 'already exists, continuing')
            continue
        else:
            map[i, j] = '#'
            print('trying new obstruction at', i, j)
            pos = pos_0
            step_count = 0
            while 0 < pos[0] < len(map[:, 0]) and 0 < pos[1] < len(map[0, :]):
                # check whether obstruction in front of guard
                if map[(pos[0]+dir[0]), (pos[1]+dir[1])] == '#':
                    #print('guard turning')
                    # rotate direction vector 90 degrees clockwise
                    dir = np.dot(dir, np.array([[0, -1], [1, 0]]))
                # walk forwards one step
                pos = pos + dir
                step_count +=1
                if step_count > 200000:
                    loop_count +=1
                    print('loops found:', loop_count)
                    break
                # add position of new step to path
                path[pos[0], pos[1]] = 1
                #print(np.sum(path))
            