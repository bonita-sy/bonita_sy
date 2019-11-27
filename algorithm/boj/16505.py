import sys

def all_print_start(index):
	for i in range(index):
		sys.stdout.write("*")
	print ""

def pongdang_start(index):
	for i in range(1, index+1):
		if (i % 2) == 1:
			sys.stdout.write("*")
		else:
			sys.stdout.write(" ")
	print ""

def even_star(index):
	ind = index / 2
	for i in range(1, ind+1):
		if (i % 2) == 1:
			sys.stdout.write("**")
		else:
			sys.stdout.write("  ")
	print ""

def end_start(index):
	for i in range(index):
		if (i == 0) or  (i == index-1):
			sys.stdout.write("*")
		else:
			sys.stdout.write(" ")
	print ""

start_num = input()

index_length = pow(2, start_num)
while index_length > 0:
	if (index_length % 4) == 0:
		all_print_start(index_length)
	elif (index_length % 4) == 3:
		pongdang_start(index_length)
	elif (index_length % 4) == 2:
		even_star(index_length)
	else:
		end_start(index_length)
	
	index_length -= 1
