import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

map = np.array([list(i) for i in data.split('\n')])
dir = np.array([-1, 0])
pos_0 = np.argwhere(map == '^').flatten()
pos = pos_0
step_count = 0
loop_count = 0
loop_pos = []

np.savetxt('map', map, fmt='%s')

for i in range(len(map[:, 0])):
    for j in range(len(map[0, :])):
        map = np.array([list(i) for i in data.split('\n')])
        step_count = 0
        dir = np.array([-1, 0])
        if map[i, j] == '#':
            print('obstruction at', i, j, 'already exists, continuing')
            continue
        else:
            map[i, j] = '#'
            print('trying new obstruction at', i, j)
            pos = pos_0
            while 0 < pos[0] < len(map[:, 0]) and 0 < pos[1] < len(map[0, :]):
                if (pos[0]+dir[0]) < 0 or (pos[0]+dir[0]) >= len(map[:, 0]) or (pos[1]+dir[1]) < 0 or (pos[1]+dir[1]) >= len(map[0, :]):
                    print('guard walking out of range, breaking')
                    break
                if map[(pos[0]+dir[0]), (pos[1]+dir[1])] == '#':
                    # rotate direction vector 90 degrees clockwise
                    dir = np.dot(dir, np.array([[0, -1], [1, 0]]))
                if map[(pos[0]+dir[0]), (pos[1]+dir[1])] == '#':
                    # rotate direction vector 90 degrees clockwise
                    dir = np.dot(dir, np.array([[0, -1], [1, 0]]))
                # walk forwards one step
                pos = pos + dir
                # yeah i know this is stupid
                if step_count < 10000:
                    step_count +=1
                else:
                    loop_count +=1
                    print('loop', loop_count, 'found at', pos[0], pos[1])
                    break

print(loop_count, 'unique obstructions result in loops')