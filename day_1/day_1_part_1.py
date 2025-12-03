from pathlib import Path

#get input
path = Path('input.txt')
rotation = path.read_text()

#turn into list
codes = rotation.splitlines()

#lists for rotation directions and ticks
direction = []
ticks = []

#starting place
dial = 50

#total times landed on 0
count = 0

#populate ticks and direction lists
for code in codes:
    direction.append(code[:1])
    ticks.append(int(code[1:]))

#turning lock
for i in range(0,len(codes)):
    if direction[i] == 'R':
        dial+= ticks[i]
        if dial >= 100:
            dial = dial %100
    else:
        dial -= ticks[i]
        if dial <= 100:
            dial = dial %100

    #check if landed on 0
    if dial == 0:
        count += 1

#answer
print(count)