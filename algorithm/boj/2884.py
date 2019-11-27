a, b = map(int, raw_input().split(" "))

if b < 45:
	a -= 1
	b += 15
else:
	b -= 45

if a < 0:
	a = 23

print str(a) + " " + str(b)
