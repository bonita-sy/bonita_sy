num = input()

for i in range(1, num+1):
	a, b = map(int, raw_input().split(" "))
	print "Case #" + str(i) + ": " + str(a) + " + " + str(b) + " = " + str(a + b)
