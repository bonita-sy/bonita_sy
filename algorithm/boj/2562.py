value_ary = []

for i in range(9):
	input_value = int(input())
	value_ary.append(input_value)

max_val = max(value_ary)
print(max_val)
print(value_ary.index(max_val) + 1)
