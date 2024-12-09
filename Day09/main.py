import re

inputTab = []
totalSize = 0 # sum of each file's size to get the optimized mmory size
memoryTab = []
checksum = 0

def createMemory():
	global totalSize
	global memoryTab
	id = 0
	for ind in range(len(inputTab)):
		
		if ind % 2 == 0: # it's a file
			for x in range(int(inputTab[ind])):
				memoryTab.append(str(id))
			id += 1
			totalSize += int(inputTab[ind])
		else: # free space
			for x in range(int(inputTab[ind])):
				memoryTab.append('.')
	
	return

def optimizeMemory():
	global memoryTab
	
	isOptimized = False
	while not isOptimized:
		ind = -1
		for i in range(len(memoryTab)): # find the first blank space
			if memoryTab[i] == '.':
				ind = i
				break
				
		if ind == -1:
			isOptimized = True
			return
		else:
			tempVal = memoryTab.pop()
			memoryTab[ind] = tempVal

	return

def	optimizeMemory_2():
	global inputTab
	global memoryTab

	size = len(inputTab)
	cursor_mem = len(memoryTab) # yes, the cursor starts outside the list
	while size > 0:
		val_inp = int(inputTab.pop()) # size  of the file block i need to move
		cursor_mem = cursor_mem - val_inp # cursor_mem - val_inp = start of the block
		
		if size % 2 == 0: # the value we just pop was freespace -> ignore
			# print("ignore free space")
			size = len(inputTab)
			continue
		
		else:
			# print(f"optimizing block {val_inp}")
			pattern = re.compile(r'\.' * val_inp)
			result = re.search(pattern, ''.join(memoryTab))
					  
			if result != None:
				# print(f"found space {result.start()} {result.end()}")
				free_indx = result.start()
			else:
				# print("no free space found")
				size = len(inputTab)
				continue

			if free_indx < cursor_mem: # if free spot is before the file that has to move
				block_id = memoryTab[cursor_mem]
				for indx in range(cursor_mem, cursor_mem + val_inp): # replace old file span with free space
					memoryTab[indx] = '.'

				for indx in range(free_indx, free_indx + val_inp): # replace old free span with file id
					memoryTab[indx] = str(block_id)
		size = len(inputTab)

def getChecksum():
	global checksum
	for i in range(len(memoryTab)):
		if memoryTab[i] == '.':
			continue
		checksum += i * int(memoryTab[i])
	return

def main():
	# filename = "inputDay09"
	filename = "test09"
	
	global inputTab
	with open(filename, "r") as file:
		for line in file:
			for char in line.strip():
				inputTab.extend(char)

	createMemory()
	# print(f"{inputTab=}")
	print(f"{memoryTab=}")
	print("###############################################")
	print("###############################################")
	print("###############################################")
	# optimizeMemory()
	optimizeMemory_2()
	print(f"{memoryTab=}")
	getChecksum()
	print(f"{checksum=}")

	return

if __name__ == "__main__":
	main()