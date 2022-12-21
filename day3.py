import string

# get the data
day3_input = open("day3_input.txt")
bag = day3_input.read()
each_bag = bag.split("\n")
day3_input.close()

# part1
'''
value = 0
for i in each_bag:
	compartment_1 = list(i[:int(len(i)/2)])
	compartment_2 = list(i[int(len(i)/2):])
	duplicate = [x for x in compartment_1 if x in compartment_2]

	if duplicate[0].isupper():
		value += ord(duplicate[0]) - 38
	if duplicate[0].islower():
		value += ord(duplicate[0]) - 96

print(value)
'''

#part2

groups = [each_bag[i:i+3] for i in range(0,len(each_bag), 3)]

value = 0
for i in groups:
	elf1, elf2, elf3 = i
	duplicate = [x for x in elf1 if x in elf2 and x in elf3]

	if duplicate[0].isupper():
		value += ord(duplicate[0]) - 38
	if duplicate[0].islower():
		value += ord(duplicate[0]) - 96

print(value)