"""This script reads in the data from a tsv, arranges both list in descinding order,
works out any differences between the numbers, then sums them up
"""

# read in the data 
col1 = []
col2 = []
with open('data/part1.txt', mode='r', encoding='utf-8') as d:
	for row in d:
		a, b, = row.strip().split()
		a = int(a)
		b = int(b)
		col1.append(a)
		col2.append(b)

# sort the values in asceding order

col1 = sorted(col1)
col2 = sorted(col2)
print(col1[0], col2[0])

answer = 0
for x, y in zip(col1, col2):
	answer += abs(x-y)

print(answer)

