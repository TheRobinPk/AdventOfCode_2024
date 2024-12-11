# Global variables
stones = {}

def blink(blk:int):
	global stones

	for b in range(blk):
		tempStones = {}
		for val in stones.keys():
			quantity = stones[val]
			stones[val] -= quantity

			# 0   ->   1
			if int(val) == 0:
				tempStones[str(1)] = (tempStones[str(1)] + quantity) if str(1) in tempStones.keys() else quantity

			# len(digit) % 2 == 0   ->   spilt
			elif len(val) % 2 == 0:
				half = len(val) // 2
				first_half = str(int(val[:half]))
				second_half = str(int(val[half:]))

				tempStones[first_half] = (tempStones[first_half] + quantity) if first_half in tempStones.keys() else quantity
				tempStones[second_half] = (tempStones[second_half] + quantity) if second_half in tempStones.keys() else quantity

			# else val * 2024
			else:
				x = int(val) * 2024
				tempStones[str(x)] = (tempStones[str(x)] + quantity) if str(x) in tempStones.keys() else quantity

		stones = tempStones
	return

def main():
	# filename = "test11"
	filename = "inputDay11"

	with open(filename, "r") as file:
		for line in file:
			tempList = line.strip().split(' ')
			for val in tempList:
				quantity = tempList.count(val)
				
				if val in stones.keys():
					stones[val] += quantity
				else:
					stones[val] = quantity
	
	print(f"{stones=}")

	blink(75)

	# print(f"{stones=}")
	total = sum(stones.values())
	print(f"Amount of stones = {total}")
	return

if __name__ == "__main__":
	main()