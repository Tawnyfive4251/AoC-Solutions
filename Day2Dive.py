'''
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

'''

#Read the instructions to a file
def read_input():
    with open('day2input.txt') as f:
        return f.readlines()
def parse_input(input):
    parsed = [x.split(' ') for x in input]
    #strip the newlines out
    stripped = []
    for i in parsed:
        i = [x.strip() for x in i]
        stripped.append(i)
    return stripped
print(parse_input(read_input()))

def move_sub(instructions, start_pos=0, start_depth=0):
    pos = start_pos
    depth = start_depth
    for i in instructions:
        if i[0] == 'forward':
            pos += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
    return pos, depth
position, depth = move_sub(parse_input(read_input()))
print("The final position is: {}".format(position))
print("The final depth is: {}".format(depth))
print("The answer to the online solution is {}".format(position*depth))

'''
Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
'''
def fixed_move_sub(instructions, start_pos=0, start_depth=0, start_aim=0):
    pos = start_pos
    depth = start_depth
    aim = start_aim
    for i in instructions:
        if i[0] == 'forward':
            pos += int(i[1])
            depth += int(i[1])*aim
        elif i[0] == 'down':
            aim += int(i[1])
        elif i[0] == 'up':
            aim -= int(i[1])
    return pos, depth

print("This is the part 2 solution")
position, depth = (fixed_move_sub(parse_input(read_input())))
print(position*depth)