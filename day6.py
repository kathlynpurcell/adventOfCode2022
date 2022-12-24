# get the data
day6_input = open("day6.txt")
input_value = day6_input.read()
day6_input.close()

'''
#part1
# find the duplicates
i = 4
communication_list = list(input_value)
while i<len(input_value):
	if len(communication_list[i-4:i]) == len(set(communication_list[i-4:i])):
		print(i)
		break
	else:
		i += 1
'''
# part 2
i = 14
communication_list = list(input_value)
while i<len(input_value):
	if len(communication_list[i-14:i]) == len(set(communication_list[i-14:i])):
		print(i)
		break
	else:
		i += 1