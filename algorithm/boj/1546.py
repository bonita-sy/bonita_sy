sub_num = int(input())
org_grade_ary = list(map(int, input().split(" ")))

max_value = max(org_grade_ary)
sum_value = 0.0

for org in org_grade_ary:
	sum_value += org / max_value * 100

print(round(sum_value / sub_num, 6))
