from pathlib import Path

#get input
path = Path('input')
input_data = path.read_text()

#turn into list
number_lines = input_data.splitlines()

#find 1st highest number
#skip pos of highest when looking for 2nd highest
#2pointer add 2 nums individully and compare
a_pointer = 0
b_pointer = 1
attempt = 0

for number in number_lines:
    #print(f'current number is: {number}')
    max = 0
    for i in range(0, len(number)):

        #print(f'comparing {number[i]}:')
        for j in range(i+1, len(number)):
         #   print(f'with {number[j]}')
            new_number = f'{number[i]}{number[j]}'
            new_sum  = int(new_number)
            if new_sum > max:
                max = new_sum
                #print(max)
        #print('end of run')
        #print(f'max is: {max}')
    attempt += max
    #print(max)

print(attempt)