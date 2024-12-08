# Global variables
ruleBook = {}
validUpdate_Counter = 0
validUpdate_midValueSum = 0
invalidUpdate_Counter = 0
invalidUpdate_midValueSum = 0
correctedLine = ""

def getRule(val:str):
	global ruleBook
	return ruleBook.get(val)

def isValidUpdate(line:str):
	tempLine = line.strip().split(',')
	size = len(tempLine)
	isValid = True
	
	# double for loop to compare a value to every next ones
	for start in range(size-1):
		rule = getRule(tempLine[start])
		if rule == None:
			continue
		
		val = start
		while val < size:
			if rule == None:
				val += 1
				continue
			if int(tempLine[val]) in rule:
				isValid = False
				tempLine[val], tempLine[start] = tempLine[start], tempLine[val]
				val = start
				rule = getRule(tempLine[val])
			else:
				val += 1

	if isValid:
		global validUpdate_Counter
		global validUpdate_midValueSum
		validUpdate_Counter += 1
		validUpdate_midValueSum += int(tempLine[int(size/2)])
	else:
		global invalidUpdate_Counter
		global invalidUpdate_midValueSum
		invalidUpdate_Counter += 1
		invalidUpdate_midValueSum += int(tempLine[int(size/2)])
		# global correctedLine
		# correctedLine = ','.join(tempLine)
		# print(f"Corrected line = {correctedLine}")
	return isValid

def main():
	"""
	Create a dictionnary of set with every rule
	rules are formatted as 'X | Y'
	dict {
		'Y0': [X0, X1, X2],
		'Y1': [X3, X4, X5]
	}
	This way I just need to check if after a Y, I find a corresponding X
		Yes -> update invalid
		No -> all good, check next
	"""

	filename = "inputDay05"
	# filename = "test05"

	global ruleBook

	with open(filename, 'r') as file:
		for line in file:
			
			if line.find('|') != -1: # finding a new rule
				tempLine = line.strip().split('|')
				tempSet = ruleBook.get(tempLine[1]) # search for Y in ruleBook
				if tempSet == None:
					tempSet = set() # create a set if Y is not already in ruleBook
				tempSet.add(int(tempLine[0]))

				ruleBook[tempLine[1]] = tempSet # updating ruleBook

			if line.find(',') != -1:
				isValidUpdate(line)
					

	print(f"Amount of valid updates = {validUpdate_Counter}")
	print(f"Sum = {validUpdate_midValueSum}")
	print("---------")
	print(f"Amount of invalid updates = {invalidUpdate_Counter}")
	print(f"Sum = {invalidUpdate_midValueSum}")
	return

if __name__ == "__main__":
	main()