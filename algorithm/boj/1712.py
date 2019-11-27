fixed_cost, variable_cost, profit = map(int, raw_input().split(" "))

if variable_cost >= profit:
	print -1
else:
	print int(fixed_cost / (profit - variable_cost)) + 1
