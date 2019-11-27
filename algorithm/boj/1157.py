word = input().upper()
word_dict = dict()

for i in word:
	if i in word_dict:
		word_dict[i] += 1
	else:
		word_dict[i] = 1

result = None
max_value = max(word_dict.values())
for key, value in word_dict.items():
	if value == max_value:
		if result is None:
			result = key
		else:
			result = "?"

print(result)
