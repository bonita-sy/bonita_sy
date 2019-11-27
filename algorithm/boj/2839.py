sugar_kg = int(input())
sugar_num = 0

while sugar_kg > 0:
	if sugar_kg % 5 != 0:
		sugar_kg -= 3
		if sugar_kg < 0:
			sugar_num = -1
			break
		sugar_num += 1
	elif sugar_kg % 5 == 0:
		sugar_num += 1
		sugar_kg -= 5
	elif sugar % 5 != 0 and sugar % 3 != 0:
		sugar_num = -1

print(sugar_num)
