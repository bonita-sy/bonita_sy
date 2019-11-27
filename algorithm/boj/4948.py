prime_list = [2, 3]

def is_prime(num):
	if num <= 1:
		return False

	i = 2
	while i*i <= num:
		if num % i == 0:
			return False
		i += 1
	
	prime_list.append(num)
	return True
	

while True:
	n = int(input())

	if n == 0:
		break

	num = 0
	new_n = n
	if prime_list[-1] <= n:
		num += len(prime_list)
		if prime_list[-1] == n:
			new_n = n + 1

	for i in range(new_n+1, n*2+1):
		if is_prime(i):
			num += 1

	print(num)
