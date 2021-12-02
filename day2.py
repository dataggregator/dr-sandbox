#day 2
convert = lambda a: (a[0], int(a[1]))

with open('inputnew') as file:
    data = [convert(line.strip().split()) for line in file]

#puzzle part 1
horizontal = depth = 0
for cmd, value in data:
    if cmd == 'forward':
        horizontal += value
    if cmd == 'down':
        depth += value
    if cmd == 'up':
        depth -= value

print (horizontal * depth)


#puzzle part 2
horizontal = depth = aim = 0
for cmd, value in data:
    if cmd == 'down': 
        aim += value
    if cmd == 'up':
        aim -= value
    if cmd == 'forward':
        horizontal += value
        depth += aim * value

print (horizontal * depth)
