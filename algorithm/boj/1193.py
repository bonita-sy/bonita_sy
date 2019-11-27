input_num = int(input())

index = 2 
cnt = 1
while cnt < input_num:
	cnt += index
	index += 1

index -= 1
cnt -= input_num

if index % 2 == 0:
	son = index - cnt
	mom = 1 + cnt
else:
	son = 1 + cnt
	mom = index - cnt

print(str(son)+"/"+str(mom))
