n, k, m = map(int, input().split(" "))
hyper_infor = {}
for i in range(1, m+1):
	hyper_infor[i] = list(map(int, input().split(" ")))
print(hyper_infor)

station_number = 0
i = 1
while True:
	for conn_stat in hyper_infor[i]:
		next_stat = i+1
		if(i == conn_stat) or (next_stat not in station_number):
			break
		if next_stat in hyper_infor[next_stat]:
			
	
for i in range(1, n+1):
	if i+1 in hyper_infor[i]:
		station_number += 1
	else:
		station_number = -1
		break

print(station_number)
