details = open('detail.json','w')

result = '{\n'

def getInput(kind):
	print('>>' + kind +':')
	string = input()
	return '"'+ kind + '": "' + string + '",\n'

def getGenre():
	print('>> genre:')
	s = input()
	s = s.split(', ')
	genre = '['
	for x in s:
		genre += '"' + x + '",'
	genre ='"genre": ' + genre[:-1] + "],\n"
	return genre




## Main Program ##
result += getInput('title')
result += getInput('author')
result += getInput('artist')
result += getInput('description')
result += getGenre()
print('\nstatus values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]')
result += getInput('status')
result += '"_status values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]\n}'
details.write(result)


