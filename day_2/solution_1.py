# read in data

input_data = []

with open('input.txt', mode='r') as d:
	for row in d:
		rows = [int(x) for x in row.strip().split()]
		input_data.append(rows)
test2 = [[1, 3, 2, 4, 5]]
answer = 0
fails_part_1 = []
print(len(input_data))

asc_func = lambda x: all(x[i] < x[i + 1] for i in range(len(x) - 1))
desc_func = lambda x: all(x[i] > x[i+1] for i in range(len(x) -1))
more_3_func = lambda x: max(abs(x[i] - x[i+1]) for i in range(len(x)-1)) <= 3
not_0_func = lambda x: all((x[i] - x[i-1]) != 0 for i in range(len(test)-1))
for test in input_data:
	
	asc = asc_func(test)
	desc = desc_func(test)
	more_3 = more_3_func(test)
	not_0 =  not_0_func(test)

	if (asc or desc) and more_3 and not_0:
		answer +=1
	else:
		fails_part_1.append(test)

print(answer)
print(len(fails_part_1))
for test in fails_part_1:
	temp_success = []
	for i in range(len(test)):
		temp_list = test.copy()
		temp_list.pop(i)
		asc2 = asc_func(temp_list)
		desc2 = desc_func(temp_list)
		more_3_2 = more_3_func(temp_list)
		not_0_2 = not_0_func(temp_list)
		#print(temp_list)
		temp_success.append((asc2 or desc2) and more_3_2 and not_0_2)
	if any(temp_success):
		answer +=1
	else:
		print(test)

print(answer)
