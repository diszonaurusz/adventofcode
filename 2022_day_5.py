import parse
import re
from typing import List
from enum import Enum

p = parse.get_input(False)

txt = p.raw_text

tst = [
    '    [D]    ',
    '[N] [C] [A]',
    '[Z] [M] [P]',
    '1   2    3',
    '',
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2'
]

def get_bound_idx(txt)->int:
    for i, line in enumerate(txt):
        if line == '':
            return i

def get_stack(txt:List[str], to:int)->List[str]:
    stack = []
    for line in txt[:to]:
        line = re.sub(r'(.{3})\s', r'\1,', line)
        line = re.sub(r'\s', '', line)
        stack.append(line.split(','))
    # Reverse stack, drop indices and remove empty elements from the top
    stack_reversed = [list(tp) for tp in (zip(*stack[-2::-1])) if tp != '']
    stack_cleaned = [[elem for elem in col if elem != ''] for col in stack_reversed]
    #stack_final = [''.join(col) for col in stack_cleaned]
    return stack_cleaned
    
def get_instructions(txt:List[str], frm:int)->List[str]:
    instr = []
    for line in txt[frm + 1:]:
        instr.append([int(val) for val in re.findall(r'\d+', line)])
    return instr

def execute_instructions(txt:List[str], ord:int)->List[str]:
    bound = get_bound_idx(txt)
    stack = get_stack(txt, bound)
    instr = get_instructions(txt, bound)

    for i in instr:
        records_to_move = stack[i[1] - 1][-i[0]:][::ord]
        del stack[i[1] - 1][-i[0]:]
        stack[i[2] - 1].extend(records_to_move)

    for q in stack:
        if q != []:
            last_elem += re.sub(r'[\[\]]', r'', q[-1])
        else:
            last_elem += ' '
    return last_elem

class ord(Enum):
    asc = 1
    desc = -1

# Part 1
print(execute_instructions(txt, ord.desc.value))

# Part 2
print(execute_instructions(txt, ord.asc.value))