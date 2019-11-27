while 1:
	a_b = raw_input()
	a, b = a_b.split(" ")
	result = int(a) + int(b)
	if result == 0:
		exit(0);
	else:
		print result
