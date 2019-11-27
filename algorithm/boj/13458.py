import math
import sys

exam_room = int(sys.stdin.readline().strip())

student_str = sys.stdin.readline().strip()
student_list = []
if " " in student_str:
	student_list = list(map(int, student_str.split(" ")))
else:
	student_list.append(int(student_str))

main, sub = map(int, input().split(" "))

need_pd = 0
for student in student_list:
	need_pd += 1
	student -= main

	if student <= 0:
		break

	need_pd += math.ceil(student / sub)

print(need_pd)
