def sum(list):
	if list == 2:
		if list[0] >= list[1]:
			return list[0]
		else:
			return list[1]
	return 1 + sum(list[1:])

print(sum([1, 2, 4]))