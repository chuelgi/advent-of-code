from pathlib import Path

count = 0

def adjustment(res):
    if res < 0:
        res += 100
        print('add 100')
        if res <= -100:
            res = res % 100
            res = abs(res)
    if res > 99:
        print('sub 99')
        res -= 99
        if res >= 100:
            res = res % 100

    return res

path = Path('input.txt')

dial = 50
rotation = path.read_text()
codes = rotation.splitlines()

#cant use dictionary because keys will be duplicated
#dictionary = {}

direction = []
ticks = []

for code in codes:
    direction.append(code[:1])
    ticks.append(int(code[1:]))

for i in range(0,len(codes)):
    if direction[i] == 'R':
       # print(direction[i])
        dial+= ticks[i]
        if dial >= 100:
            dial = dial %100
    else:
        #print(direction[i])
        dial -= ticks[i]
        if dial <= 100:
            dial = dial %100
    print(dial)
    if dial == 0:
        count += 1
   # print(f'before adjust: {dial}')
    #dial = adjustment(dial)
    #print(f'after adjust: {dial}')


print(dial)
print(count)