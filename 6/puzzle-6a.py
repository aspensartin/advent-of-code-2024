import numpy as np

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

map = np.array([list(i) for i in data.split('\n')])
map_visits = map
path = np.zeros_like(map, dtype='int')    
dir = np.array([-1, 0])
pos = np.argwhere(map == '^').flatten()

path[pos[0], pos[1]] = 1
map_visits[pos[0], pos[1]] = 'X'   

while 0 < pos[0] < len(map[:, 0]) and 0 < pos[1] < len(map[0, :]):
    if (pos[0]+dir[0]) < 0 or (pos[0]+dir[0]) >= len(map[:, 0]) or (pos[1]+dir[1]) < 0 or (pos[1]+dir[1]) >= len(map[0, :]):
        print('guard walking out of range, breaking')
        break
    # check whether obstruction in front of guard
    if map[(pos[0]+dir[0]), (pos[1]+dir[1])] == '#':
        print('guard turning')
        # rotate direction vector 90 degrees clockwise
        dir = np.dot(dir, np.array([[0, -1], [1, 0]]))
    # walk forwards one step
    pos = pos+dir
    # add position of new step to path
    path[pos[0], pos[1]] = 1
    map_visits[pos[0], pos[1]] = 'X'
    print(np.sum(path))

np.savetxt('map.txt', map_visits, fmt='%s', delimiter='')