with open('./input/day3.txt') as fin:
    input = [str(i) for i in fin.read().strip().split("\n")]

def part1():
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    one = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = ''
    epsilon = ''
    for bin in input:
        for i in range(len(bin)):
            if int(bin[i]) == 1:
                one[i] += 1
            else:
                zero[i] +=1
    
    for n in range(len(one)):
        if one[n] > zero[n]:
            gamma += '1'
            epsilon += '0'
        else: 
            gamma += '0'
            epsilon += '1'
    print(int(gamma,2) * int(epsilon,2))
         




part1()