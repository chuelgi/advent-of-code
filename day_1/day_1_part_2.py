from pathlib import Path

#get input
path = Path('fake_input')
rotation = path.read_text()

#turn into list
codes = rotation.splitlines()
#codes = ['L68', 'L30', 'R48', 'L5','R60','L55','L1', 'L99','R14','L82']

#lists for rotation directions and ticks
direction = []
ticks = []

#starting place
dial = 50

#total times landed on 0 and past 0
count = 0

#populate ticks and direction lists
for code in codes :
    direction.append(code[:1])
    ticks.append(int(code[1:]))

#turning lock
for i in range(0,len(codes)):

    if direction[i] == 'R':
        print(f'increase {i}')
        dial+= ticks[i]
        if dial >= 100:
            count += dial // 100
            dial = dial % 100
            print(f'dial: {dial}')
        if dial == 0:
            count += 1

    else:
        print(f'decrease {i}')
        current_dial = dial
        count += (ticks[i] - current_dial+99) // 100
        dial = (dial - ticks[i]) % 100

        if dial == 0:
            count += 1

    print('end of iteration')

    print(f'current count: {count}')
#answer
print(f'answer: {count}')
