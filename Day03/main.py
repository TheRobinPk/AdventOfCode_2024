import re
mulList = []
totalMul = 0

def findTotalMul_1():
	global mulList
	global totalMul
	for mul in mulList:
		tempMul = mul.strip("mul()").split(',')
		totalMul += int(tempMul[0]) * int(tempMul[1])

def findTotalMul_2():
	global mulList
	global totalMul
	isDo = True

	for mul in mulList:
		if re.match(r'don\'t\(\)', mul) != None:
			isDo = False
			continue
		if re.match(r'do\(\)', mul) != None:
			isDo = True
			continue
		
		if isDo:
			tempMul = mul.strip("mul()").split(',')
			totalMul += int(tempMul[0]) * int(tempMul[1])
	
	return

def main():
	# filename = "test03"
	filename = "inputDay03"

	# Finding all vamid mul in file
	# keeping "mul(x,y)" as string in mulList
	global mulList
	with open(filename, "r") as file:
		for line in file:
			# mulList.extend(re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)) # Part 1

			'''
			Part 2 :
			mulList.extend(re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', line))
			returns a tuple with 3 entries, either '' or the matching value of mul(x,y), don't() and do()
			
			Exemples:
			('mul(339,896)', '', '')
			('', 'do()', '')
			('', '', "don't()")

			So i can't just append it to mulList
			'''

			# Part 2
			result = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', line) 
			for tup in result:
				for val in tup:
					if val != '':
						mulList.append(val)

	print(mulList)
	# findTotalMul_1()
	findTotalMul_2()
	global totalMul
	print(f"total = {totalMul}")
	return

if __name__ == "__main__":
	main()