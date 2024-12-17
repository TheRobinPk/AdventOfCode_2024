# Global variables
map = []
booleanMap = []
regions = []

def findRegions():
	global regions
	
	# for x in range(len(map[0])):
	# 	for y in range(len(map)):
			

	return

def main():
	filename = "test12"
	# filename = "inputDay12"

	with open(filename, "r") as file:
		for line in file:
			tempLine = []
			tempLineBool = []
			for char in line.strip():
				tempLine.apppend(char)
				tempLineBool.apppend(0)
			map.append(tempLine)
	
	findRegions()

	return

if __name__ == "__main__":
	main()