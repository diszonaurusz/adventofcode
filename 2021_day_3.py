import parse
from math import floor

p = parse.get_input(True)
txt = p.raw_text

tst = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

def get_str_score(score):
    return ''.join([str(val) for val in score])

def get_decimal_score(score):
    return int(score, 2)

# Part 1
def get_score_pt1(inp):

    line_len = len(inp[0])
    counter = 0
    char_sum = [0] * line_len

    for line in inp:
        counter += 1
        for i, c in enumerate(line):
            char_sum[i] += int(c)

    gamma = [1 if val > (counter / 2) else 0 for val in char_sum]
    epsilon = [1 if val == 0 else 0 for val in gamma]
    return [get_str_score(gamma), get_str_score(epsilon)]


part_1_score = [get_decimal_score(val) for val in get_score_pt1(txt)]

print(f'Part 1:\n- Gamma: {part_1_score[0]}\n- Epsilon: {part_1_score[1]}\n- Product: ' + str(part_1_score[0] * part_1_score[1]))

# Part 2
def get_score_pt2(inp, typ):

    line_len = len(inp[0])
    char_sum = [0] * line_len
    char_list = ''

    for i in range(0, line_len):
        rec_cnt = len(inp)
        for j in range(0, rec_cnt):
            elem = (inp[j])[i]
            char_sum[i] += int(elem)
        if rec_cnt == 1:
            char_list += elem
        elif char_sum[i] == rec_cnt / 2:
            char_list += str(typ)
        else:
            char_list += str(int(int(char_sum[i] > (rec_cnt / 2)) == typ))
        inp = [val for val in inp if val[:i + 1] == char_list]
        print(char_list, len(inp), inp)
        
    return(char_list)
    
co2 = get_decimal_score(get_score_pt2(tst, 0))

oxygen, co2 = get_decimal_score(get_score_pt2(txt, 1)), get_decimal_score(get_score_pt2(txt, 0))

print(f'Part 2:\n- Oxygen generator: {oxygen}\n- CO2 scrubber: {co2}\n- Product: ' + str(oxygen * co2))
