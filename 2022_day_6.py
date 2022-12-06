import parse
import re
from typing import List

inp = parse.get_input(False)
txt = inp.raw_text[0]

def decode_regex(txt:str, dist_len:int)->List[str]:
    for i, c in enumerate(txt):
        if re.match(r'^(?:([A-Za-z])(?!.*\1)){' + str(dist_len) + r'}$', txt[i: i + dist_len]):
            return i + dist_len, txt[i: i + dist_len]

def decode_loop(txt:str, dist_len:int)->List[str]:
    for i, c in enumerate(txt):
        if len(set(txt[i: i + dist_len])) == dist_len:
            return i + dist_len, txt[i:i + dist_len]

# Part 1
print(decode_regex(txt, 4))
print(decode_loop(txt, 4))

# Part 2
print(decode_regex(txt, 14))
print(decode_regex(txt, 14))