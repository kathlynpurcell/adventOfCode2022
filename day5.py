# get the data
day5_input = open("day5_input.txt")
moves = day5_input.read()
each_move = moves.split("\n")
day5_input.close()


first_state_str = """
                        [Z] [W] [Z]
        [D] [M]         [L] [P] [G]
    [S] [N] [R]         [S] [F] [N]
    [N] [J] [W]     [J] [F] [D] [F]
[N] [H] [G] [J]     [H] [Q] [H] [P]
[V] [J] [T] [F] [H] [Z] [R] [L] [M]
[C] [M] [C] [D] [F] [T] [P] [S] [S]
[S] [Z] [M] [T] [P] [C] [D] [C] [D]
 1   2   3   4   5   6   7   8   9 
"""

current_state = [["N","V","C","S"],["S","N","H","J","M","Z"],["D","N","J","G","T","C","M"],
				["M","R","W","J","F","D","T"],["H","F","P"],["J","H","Z","T","C"],
				["Z","L","S","F","Q","R","P","D"],["W","P","F","D","H","L","S","C"],["Z","G","N","F","P","M","S","D"]]

# part1
'''
# break up the string
for line in each_move:
	line = line.split(" ")
	number_of_boxes = int(line[1])
	from_column = int(line[3]) - 1
	to_column = int(line[5]) - 1
	while number_of_boxes:
		current_state[to_column].insert(0, current_state[from_column][0])
		current_state[from_column].pop(0)
		number_of_boxes = number_of_boxes - 1

print("".join([i[0] for i in current_state]))
'''

# part2
# break up the string
for line in each_move:
	line = line.split(" ")
	number_of_boxes = int(line[1]) 
	from_column = int(line[3]) - 1
	to_column = int(line[5]) - 1
	for i in range(number_of_boxes):
		current_state[to_column].insert(i, current_state[from_column][0])
		current_state[from_column].pop(0)

print("".join([i[0] for i in current_state]))