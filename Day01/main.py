leftCol = []
rightCol = []


def sortLists():
	global leftCol
	global rightCol
	size = len(leftCol)

	# Bubble sort
	for i in range(size-1):
		for j in range(i+1, size):
			return
	return	


	return

def main():
	filename = "test01"
	# filename = "inputDay01"

	with open(filename, "r") as file:
		for line in file:
			tempLine = line.strip().split("   ")
			leftCol.append(tempLine[0])
			rightCol.append(tempLine[1])

	sortLists()



if __name__ == "__main__":
	main()