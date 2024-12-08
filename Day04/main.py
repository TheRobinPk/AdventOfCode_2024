# Global variables
word = "MAS"
wordsize = len(word) - 1
linesTab = []
width = 0
height = 0
wordCounter = 0

# ===== HORIZONTAL =====
def searchHorizontal_LR(line:int, col:int, size:int):
	if col >= width:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchHorizontal_LR(line, col+1, size+1)
	return False

def searchHorizontal_RL(line:int, col:int, size:int):
	if col < 0:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchHorizontal_RL(line, col-1, size+1)
	return False

# ====== VERTICAL ======
def searchVertical_UD(line:int, col:int, size:int):
	if line >= height:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchVertical_UD(line+1, col, size+1)
	return False

def searchVertical_DU(line:int, col:int, size:int):
	if line < 0:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchVertical_DU(line-1, col, size+1)
	return False

# ====== DIAGONAL ======
def searchDiagonal_LR_UD(line:int, col:int, size:int): # \>
	if line >= height or line < 0 or col >= width or col < 0:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchDiagonal_LR_UD(line+1, col+1, size+1)
	return False

def searchDiagonal_LR_DU(line:int, col:int, size:int): # />
	if line >= height or line < 0 or col >= width or col < 0:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchDiagonal_LR_DU(line-1, col+1, size+1)
	return False

def searchDiagonal_RL_UD(line:int, col:int, size:int): # </
	if line >= height or line < 0 or col >= width or col < 0:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchDiagonal_RL_UD(line+1, col-1, size+1)
	return False

def searchDiagonal_RL_DU(line:int, col:int, size:int): # <\
	if line >= height or line < 0 or col >= width or col < 0:
		return False
	if size == wordsize and linesTab[line][col] == word[size]:
		return True
	if linesTab[line][col] == word[size]:
		return False or searchDiagonal_RL_DU(line-1, col-1, size+1)
	return False


def searchForWord(line:int, col:int):
	global wordCounter
	wordCounter+=1 if searchHorizontal_LR(line, col, 0) else 0
	wordCounter+=1 if searchHorizontal_RL(line, col, 0) else 0

	wordCounter+=1 if searchVertical_UD(line, col, 0) else 0
	wordCounter+=1 if searchVertical_DU(line, col, 0) else 0

	wordCounter+=1 if searchDiagonal_LR_UD(line, col, 0) else 0
	wordCounter+=1 if searchDiagonal_LR_DU(line, col, 0) else 0
	wordCounter+=1 if searchDiagonal_RL_UD(line, col, 0) else 0
	wordCounter+=1 if searchDiagonal_RL_DU(line, col, 0) else 0

def searchForCross(line:int, col:int):
	crossCounter = 0

	crossCounter+=1 if searchDiagonal_LR_UD(line-1, col-1, 0) else 0
	crossCounter+=1 if searchDiagonal_LR_DU(line+1, col-1, 0) else 0
	crossCounter+=1 if searchDiagonal_RL_UD(line-1, col+1, 0) else 0
	crossCounter+=1 if searchDiagonal_RL_DU(line+1, col+1, 0) else 0

	global wordCounter
	wordCounter+=1 if crossCounter == 2 else 0

def main():
	filename = "inputDay04"

	# Store file content into double entry array
	global linesTab
	with open(filename, "r") as file:
		for line in file:
			linesTab.append(line.strip())
	
	global height
	height = len(linesTab)
	global width
	width = len(linesTab[0])
	print(f"{height} {width}")

	# Finding all 'X'
	for line in range(height):
		for col in range(width):
			if linesTab[line][col] == word[1]:
				# searchForWord(line, col)
				searchForCross(line, col)
	
	print(f"wordCounter = {wordCounter}")

if __name__ == "__main__":
	main()