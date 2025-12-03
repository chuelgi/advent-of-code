from pathlib import Path

#get input
path = Path('day_2_input')

inputs = path.read_text()
examples = ('11-22,95-115,998-1012,1188511880-1188511890,'
           '222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,'
           '824824821-824824827,2121212118-2121212124')

individual = ''

ranges = inputs.split(',')
#print(ranges)
#ranges = ['11-22', '95-115','998-1010',
#           '1188511880-1188511890','222220-222224','1698522-1698528',
#          '446443-446449','38593856-38593862']

#turn into ints

#find dash index
dash = 0
def find_ranges(range_list):
    dash = range_list.index('-')

    # use dash to get starting num and ending num
    start = range_list[:dash]
    end = range_list[dash+1:]

    return start, end

def compare_strings(start,end):
    total = 0
    for k in range(int(start), int(end)+1):
        #print(k)

         #turn into string
        number_string = str(k)
        #if string length is odd go to next number
        if len(number_string) %2 != 0:
            #print(f'{stg}not even')
            continue
        #split in half
        length = len(number_string) // 2
        #print(length)
        #compare halves
        #print(f'number is: {stg} first half:{stg[:length]} second half: {stg[length:]}')

        if number_string[:length] == number_string[length:]:
            total += k
            #print(f'number is: {number_string} first half:{number_string[:length]} second half: {number_string[length:]}')
            #print(f'{number_string[:length]} equals {number_string[length:]}')
    return total

res = 0
for i in range(0, len(ranges)):


    range_pair = find_ranges(ranges[i])
    print(range_pair)
    res += compare_strings(range_pair[0],range_pair[1])

print(res)
print(f'list length {len(ranges)}')