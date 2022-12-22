"""
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
"""

# get the data
day4_input = open("day4_input.txt")
pairs = day4_input.read()
each_pair = pairs.split("\n")
day4_input.close()

# part1
'''
# isolate each elf
increment = 0
elf_ranges = [i.replace("-",",").split(",") for i in each_pair]
for j in elf_ranges:
	j = [int(i) for i in j]
	if j[0] <= j[2] and j[1] >= j[3]:
		# elf1 does all the work of elf2
		increment += 1
	elif j[2] <= j[0] and j[3] >= j[1]:
		# elf2 does all the work of elf1
		increment += 1
print(increment)
'''
#part2
increment = 0
elf_ranges = [i.replace("-",",").split(",") for i in each_pair]
for j in elf_ranges:
	j = [int(i) for i in j]
	if j[0] <= j[2] and j[1] >= j[2]:
		# elf1 does all the work of elf2
		increment += 1
	elif j[2] <= j[0] and j[3] >= j[0]:
		# elf2 does all the work of elf1
		increment += 1
print(increment)