import random


lst = []
for i in range(10):
    number = random.randint(0, 101) 
    lst.append(number)
print("lst = ", lst)


with open('file.txt', 'w') as f:
    s = str(len(lst))
    f.write(s + '\n')
    for i in lst:
        s = str(i) 
        f.write(s + ' ')


with open('file.txt', 'r+') as f:
    s = f.readline()
    lst2 = []
    for line in f:
        strs = line.split()
        for s in strs:
            if s != '':
                lst2.append(int(s))
    print('lst2=', lst2)
    total = sum(x for x in lst2 if x >= 9)
    print('Cut ededler:', [x for x in lst2 if x >= 9])
    f.write('\nToplam: ' + str(total))
