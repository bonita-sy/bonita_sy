num_ary = list()

for i in range(10):
	remain_value = int(input()) % 42
	if remain_value not in num_ary:
		num_ary.append(remain_value)

print(len(num_ary))
