def ifValid(line):
	numZero = 0
	numOne = 0
	# print(line)

	for c in line:
		if c == '0':
			numZero += 1
		else:
			numOne += 1
	return (numOne % 2 == 0) | (numZero % 3 == 0)

def findNumOfBits(fileName):

	retVal = 0
	with open(fileName, "r") as txtFile:
		lines = txtFile.readlines()
		# print(lines)
		for line in lines:
			if ifValid(line.strip()):
				retVal += 1
	return retVal

if __name__ == "__main__":
	print(findNumOfBits('data.dat'))