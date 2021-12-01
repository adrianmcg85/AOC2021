

def part1():
    input =  open('./input/day1.txt', 'r').readlines()
    count = 0
    prev = 0
    for x in input:
        if int(x) > int(prev):
            count += 1
        prev = x
    print(count)

part1()

def part2():
    with open('./input/day1.txt') as fin:
        input = [int(i) for i in fin.read().strip().split("\n")]

    count = 0
    prev_win = 1000000000
    cur_win = sum(input[:3])
    for i in range(len(input) - 3):
        if cur_win > prev_win:
            count += 1

        prev_win = cur_win
        
        cur_win -= input[i]
        cur_win += input[i + 3]

    if cur_win > prev_win:
        count += 1

    print(count)


part2()