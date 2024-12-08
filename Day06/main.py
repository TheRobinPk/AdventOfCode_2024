# Global variables
map = []
guard = (0,0)
direction = "up" # up, down, left, right
travelDistance = 1
loopingObstacles = []

def findGuard():
	global map
	global guard

	for y in range(len(map)):
		for x in range(len(map[0])):
			if map[x][y][0] == '^':
				guard = (x, y)
				map[x][y] = ['X', ["up"]]
				return
	
	print("guard not found")
	return

def guardPatrol():
	global map
	global guard
	global direction
	global travelDistance
	global loopingObstacles

	isInsideMap = True
	while isInsideMap:
		(x, y) = guard
		
		match direction:
			case "up":
				# Part 2
				try:
					i = y+1
					while i < len(map[0]):
						if map[x][i][0] == '#':
							break
						if "right" in map[x][i][1]:
							if map[x-1][y][0] != '#' and (x-1,y) not in loopingObstacles:
								loopingObstacles.append((x-1,y))
								break
						else:
							i += 1
				except:
					None
			
				try:
					if map[x-1][y][0] == 'X':
						guard = (x-1, y)
						map[x][y][0] = 'X'
					elif map[x-1][y][0] == '.':
						guard = (x-1, y)
						travelDistance += 1
						map[x][y][0] = 'X'
					else:
						direction = "right"
					map[x][y][1].append("up")

				except:
					print("Going OOB")
					isInsideMap = False
			
			case "right":
				# Part 2
				try:
					i = x+1
					while i < len(map):
						if map[i][y][0] == '#':
							break
						if "down" in map[i][y][1]:
							if map[x][y+1][0] != '#' and (x,y+1) not in loopingObstacles:
								loopingObstacles.append((x,y+1))
								break
						else:
							i += 1
				except:
					None

				try:
					if map[x][y+1][0] == 'X':
						guard = (x, y+1)
						map[x][y][0] = 'X'
					elif map[x][y+1][0] == '.':
						guard = (x, y+1)
						travelDistance += 1
						map[x][y][0] = 'X'
					else:
						direction = "down"
					map[x][y][1].append("right")
					
				except:
					print("Going OOB")
					isInsideMap = False
			
			case "down":
				# Part 2
				try:
					i = y-1
					while i >= 0:
						if map[x][i][0] == '#':
							break
						if "left" in map[x][i][1]:
							if map[x+1][y][0] != '#' and (x+1,y) not in loopingObstacles:
								loopingObstacles.append((x+1,y))
								break
						else:
							i -= 1
				except:
					None

				try:
					if map[x+1][y][0] == 'X':
						guard = (x+1, y)
						map[x][y][0] = 'X'
					elif map[x+1][y][0] == '.':
						guard = (x+1, y)
						travelDistance += 1
						map[x][y][0] = 'X'
					else:
						direction = "left"
					map[x][y][1].append("down")
					
				except:
					print("Going OOB")
					isInsideMap = False
			
			case "left":
				# Part 2
				try:
					i = x-1
					while i >= 0:
						if map[i][y][0] == '#':
							break
						if "up" in map[i][y][1]:
							if map[x][y-1][0] != '#' and (x,y-1) not in loopingObstacles:
								loopingObstacles.append((x,y-1))
								break
						else:
							i -= 1
				except:
					None

				try:
					if map[x][y-1][0] == 'X':
						guard = (x, y-1)
						map[x][y][0] = 'X'
					elif map[x][y-1][0] == '.':
						guard = (x, y-1)
						travelDistance += 1
						map[x][y][0] = 'X'
					else:
						direction = "up"
					map[x][y][1].append("left")

				except:
					print("Going OOB")
					isInsideMap = False
			
			case _:
				print("Direction Error")
				return
		
		# print(f"{loopingObstacles=}", end='\r')
	return

def main():
	# filename = "inputDay06"
	filename = "test06"

	'''
	Part 2:
	At every cell, i will store a list of direction that was used by the guard on that cell.
	While iterating i will check if the cells to the right as already been used for that "turn-right" direction.
	If so, it means i found an obstacle in the cell right in front of me.
	As a safety, i will also store every possible position for an obstacle to ensure i won't count duplicates.
	'''

	# transform input map into 2 entry list
	global map
	with open(filename, "r") as file:
		for line in file:
			tempLine = []
			for i in range(len(line.strip())):
				tempLine.append([line[i], []])
			map.append(tempLine)

	# find starting position
	findGuard()

	guardPatrol()
	
	# Calculate the maximum width of a cell
	max_width = max(len(str(cell)) for row in map for cell in row)

	for row in map:
		for cell in row:
			# Format the cell string
			cell_str = f"{cell[0]} ({', '.join(cell[1])})"
			print(cell_str.ljust(max_width), end=' ')
		print()
	
	global travelDistance
	# print(f"{travelDistance=}")
	print(f"{len(loopingObstacles)=}")
	print(f"{loopingObstacles=}")

	return

# ['X', ['down', 'left']]

if __name__ == "__main__":
	main()