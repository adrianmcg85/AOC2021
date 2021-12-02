def part1():
    with open('./input/day2.txt') as fin:
        input = [str(i) for i in fin.read().strip().split("\n")]
    y = 0
    x = 0
    for i in input:
        arr = i.split(' ')
        move = int(arr[1])
        if arr[0] == 'forward':
            x += move
        elif arr[0] == 'down':
            y += move
        elif arr[0] == 'up':
            y -= move
    print(x*y)

part1()