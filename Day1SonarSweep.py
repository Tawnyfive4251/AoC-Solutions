#AoC 2021 Day 1: Sonar Sweep

#read the input file lines, store it in a list.
with open('Day1SonarSweepData.txt') as f:
    data = f.readlines()
    data= [int(x) for x in data]

#figure out how quickly the depth increases
#and how many times the range is increased
def iterate_depth(data):
    n_increased = 0
    n_decreased = 0
    for i in range(1, len(data)):
        if data[i]>data[i-1]:
            n_increased += 1
        elif data[i]<data[i-1]:
            n_decreased += 1
    print(n_increased, n_decreased)
    return n_increased, n_decreased

def sliding_depth_read(data):
    sum_list = []
    for i in range(2, len(data)):
        sum_list.append(data[i] + data[i-1] + data[i-2])
    iterate_depth(sum_list)
#Call the functions on the data
iterate_depth(data)
sliding_depth_read(data)