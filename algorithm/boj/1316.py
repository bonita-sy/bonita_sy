def chk_word(word):
	eword_ary = list()
	result = 1

	for w in word:
		if w in eword_ary:
			if(eword_ary.index(w) != (len(eword_ary)-1)):
				result = 0
				break
		else:
			eword_ary.append(w)

	return result
		
	
num = int(input())
result_num = 0

for i in range(num):
	word = input()
	result_num += chk_word(word)

print(result_num)
