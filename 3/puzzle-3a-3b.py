import re

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

chunked_data = data.split('do()')
enabled_data = str()
for i in chunked_data:
    if "don't()" in i:
            i = i[:i.find("don't()")]
    enabled_data +=i

def muls(stuff):
    digits = re.findall('(?<=mul\\()[0-9]{1,3},[0-9]{1,3}(?=\\))', stuff)
    return sum([int(i.split(',')[0]) * int(i.split(',')[1]) for i in digits])

print('Total is', muls(data))
print('Total is', muls(enabled_data), "accounting for do() and don't() operations")