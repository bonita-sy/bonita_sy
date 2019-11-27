croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for cro in croatia:
	word = word.replace(cro, 'A');

print(len(word))
