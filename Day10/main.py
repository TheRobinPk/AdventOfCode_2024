map = []
trailHeads = []
trailEnds = []
totalScore = 0

def findTrailHeads():
	global trailHeads

	for x in range(len(map[0])):
		for y in range(len(map)):
			if map[y][x] == '0':
				trailHeads.append((y,x))
	return

def checkTop(y, x, pos):
	try:
		if y != 0 and int(map[y-1][x]) == (pos+1):
			# print(f"valid path [{y}][{x}]={pos}  ------> [{y-1}][{x}]={pos+1}")
			return True
		return False
	except:
		return False

def checkBottom(y, x, pos):
	try:
		if int(map[y+1][x]) == (pos+1):
			# print(f"valid path [{y}][{x}]={pos}  ------> [{y+1}][{x}]={pos+1}")
			return True
		return False
	except:
		return False
	
def checkRight(y, x, pos):
	try:
		if int(map[y][x+1]) == (pos+1):
			# print(f"valid path [{y}][{x}]={pos}  ------> [{y}][{x+1}]={pos+1}")
			return True
		return False
	except:
		return False

def checkLeft(y, x, pos):
	try:
		# print(f"try path [{y}][{x}]={pos}  ------> [{y}][{x-1}]={pos+1}")
		if x != 0 and int(map[y][x-1]) == (pos+1):
			return True
		return False
	except:
		return False

def findHeadScore(y:int, x:int, pos:int = 0, score:int = 0):
	global trailEnds
	# terminal condition
	if pos == 9 and (y,x) not in trailEnds:
		# trailEnds.append((y,x)) # Part 1 only 
		# print("finished trail")
		return 1
	
	top = findHeadScore(y-1, x, pos+1, score) if checkTop(y, x, pos) else 0	
	bottom = findHeadScore(y+1, x, pos+1, score) if checkBottom(y, x, pos) else 0
	right = findHeadScore(y, x+1, pos+1, score) if checkRight(y, x, pos) else 0	
	left = findHeadScore(y, x-1, pos+1, score) if checkLeft(y, x, pos) else 0
 
	return top + bottom + right + left

def findTrails():
	global totalScore
	global trailEnds

	for head in trailHeads:
		y = head[0]
		x = head[1]
		# trailEnds = [] # Part 1 : reset trailEnds so i don't count duplicate endings from the same head
		totalScore += findHeadScore(y, x)
	return

def main():
	# filename = "test10"
	filename = "input10"

	global map
	with open(filename, "r") as file:
		for line in file:
			tempLine = []
			for char in line.strip():
				tempLine.append(char)
			map.append(tempLine)

	findTrailHeads()

	findTrails()

	print(f"{totalScore=}")
	return

if __name__ == "__main__":
	main()