import re

with open('input.txt', 'r') as input:
    data = input.read()
    input.close()

muls = re.findall('mul\\([0-9]{1,3},[0-9]{1,3}\\)', data)
digits = re.findall('\d+', ' '.join(muls))
total = sum([int(i)*int(j) for i,j in zip(digits[::2], digits[1::2])])
print('Total is', total)

chunked_data = data.split('do()')
enabled_data = str()
for i in chunked_data:
    if "don't()" in i:
            i = i[:i.find("don't")]
    enabled_data +=i

muls_2 = re.findall('mul\\([0-9]{1,3},[0-9]{1,3}\\)', enabled_data)
digits_2 = re.findall('\d+', ' '.join(muls_2))
total_2 = sum([int(i)*int(j) for i,j in zip(digits_2[::2], digits_2[1::2])])
print('Total is', total_2, "accounting for do() and don't() operations")
