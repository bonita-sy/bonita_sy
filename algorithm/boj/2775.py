test_case = int(input())

for i in range(test_case):
	k_floor = int(input())
	n_room = int(input())

	k_list = []
	for k in range(k_floor):
		tmp_list = [];
		for n in range(1, n_room+1):
			if len(k_list) == 0:
				tmp_list.append(n)
			else:
				tmp_list.append(sum(k_list[:n]))
		k_list = tmp_list

	print(sum(k_list[:n_room+1]))
		
		
	
