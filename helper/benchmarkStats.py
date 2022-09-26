import sys


def countPauseTime(line):
    global pauseTime
    pos = line.find('pause')
    if pos == -1:
        return
    pos = pos + 6
    ms = eval(line[pos:pos+3])
    pauseTime += ms * 10


def countCollections(line):
    global collections
    pos = line.find('promoted')
    if pos == -1:
        return
    pos = pos + len('promoted=')
    i = pos + 1
    while line[pos:i].isdigit():
        i += 1
    promoted = eval(line[pos:i-1])
    pos = line.find('semi_space_copied')
    pos = pos + len('semi_space_copied=')
    i = pos + 1
    while line[pos:i].isdigit():
        i += 1
    copied = eval(line[pos:i-1])
    # print(promoted, copied)
    collections += promoted
    collections += copied


pauseTime = 0
collections = 0
filepath = sys.argv[1]

with open(filepath, 'r') as file:
    lines = file.readlines()
    for line in lines:
        countPauseTime(line)
        countCollections(line)
    file.close()

print('Pause Time:', pauseTime / 10)
print('Number of Collections:', collections)