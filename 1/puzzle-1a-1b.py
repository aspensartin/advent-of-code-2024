with open('input.txt', 'r') as input:
    data = input.read().split()
    input.close()

left = sorted(data[::2])
right = sorted(data[1::2])
distance = sum([abs(int(a)-int(b)) for a,b in zip(left, right)])
similarity = sum([right.count(a)*int(a) for a in left])

print('Distance between lists is', distance)
print('Similarity of lists is', similarity)

