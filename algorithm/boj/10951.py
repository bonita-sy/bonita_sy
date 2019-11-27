from sys import stdin
lines = stdin.readlines()
for line in lines:
		a, b = line.split(" ")
		print int(a) + int(b)
