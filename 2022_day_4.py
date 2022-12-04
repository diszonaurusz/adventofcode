import parse

p = parse.get_input()
txt = p.raw_text

tst = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]

def prepare_txt(txt):
    return [(list(map(int, a.split('-'))), list(map(int, b.split('-')))) for a, b in [t.split(',') for t in txt]]

def cnt_of_fully_overlapping_pairs(txt):
    counter = 0
    for a, b in txt:
        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            counter += 1
    return counter

def cnt_of_overlapping_pairs(txt):
    counter = 0
    for a, b in txt:
        set_1 = set([a for a in range(a[0], a[1] + 1)])
        set_2 = set([b for b in range(b[0], b[1] + 1)])
        if set_1.intersection(set_2):
            counter += 1
    return counter

def print_results(part:int):
    if part == 1:
        tst_overlap_cnt = cnt_of_fully_overlapping_pairs(prepare_txt(tst))
        overlap_cnt = cnt_of_fully_overlapping_pairs(prepare_txt(txt))
    if part == 2:
        tst_overlap_cnt = cnt_of_overlapping_pairs(prepare_txt(tst))
        overlap_cnt = cnt_of_overlapping_pairs(prepare_txt(txt))

    print(f'Part {part}:\n- Test overlap count: {tst_overlap_cnt}\n- Overlap count: {overlap_cnt}')

for i in range(1, 3):
    print_results(i)