origin_num = int(input())

if not(0 <= origin_num <= 99):
	exit()
else:
	new_num = origin_num
	index = 0

	while True:
		ten_num = 0
		one_num = new_num
		if (new_num > 9):
			ten_num = int(new_num / 10)
			one_num = new_num % 10

		sum_num = ten_num + one_num
		if (sum_num > 9):
			sum_num %= 10

		new_num = sum_num
		if (one_num > 0):
			new_num += (10 * one_num)

		index += 1
		if (new_num == origin_num):
			break;
	print(index)
