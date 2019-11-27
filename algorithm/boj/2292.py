number= int(input())

room_num = 1
room_cnt = 1
while True:
	if room_num < number:
		room_num += (6 * room_cnt)
		room_cnt += 1
	else:
		break

print(room_cnt)
