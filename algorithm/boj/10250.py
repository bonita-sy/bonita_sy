num = int(input())

for i in range(num):
	h, w, n = map(int, input().split(" "))

	if n <= h:
		print(n*100+1)
	else:
		end_num = 1
		while n > 0:
			n -= h
			end_num += 1
			if n <= h:
				break
		print(n*100 + end_num)
			
