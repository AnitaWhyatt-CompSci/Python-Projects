#Cpts 481 Python Software
#Homework #2 Problem #1
#Student: Anita Whyatt


from concordance import concordance
import sys


numberOfFiles = len(sys.argv)
listOfFiles = sys.argv[1:]
masterDict = {}


def addToMasterDict(addDict, filename):
	#print(addDict) #{'flim': [1, 2, 3], 'flam': [1, 1, 2]}
	#print(filename)
	for item in addDict:
		#print(item) #flim/flam
		#print(addDict[item]) #[1,2,3]
		if item not in masterDict:
			masterDict[item] = [ {filename: addDict[item]} ]
		elif item in masterDict:
			masterDict[item].append( {filename: addDict[item]} )


def formatFrequentNumbers(inputList):
	returnString = ""
	reviewedNumbers = {}
	for num in inputList:
		if num in reviewedNumbers:
			reviewedNumbers[num] += 1
		elif num not in reviewedNumbers:
			reviewedNumbers[num] = 1
	#print(inputList)
	#print(reviewedNumbers)
	for item in reviewedNumbers:
		if reviewedNumbers[item] == 1:
			returnString += f"{item}, "
		else:
			returnString += f"{item}({reviewedNumbers[item]}), "
		#print(item, reviewedNumbers[item])
		#print(returnString)
	return(returnString)


def finalPrint(alphaMasterDict):
	print("\n\nFinal Print:\n")
	#print out final dictionary in desired format
	for wordDict in alphaMasterDict:
		totalAppearances = 0
		#print("wordDict: ", wordDict)
		for fileDict in alphaMasterDict[wordDict]:
			#print("    fileDict: ", fileDict)
			for fileTitle in fileDict:
				#print("        fileDict[fileTitle]: ",fileDict[fileTitle])
				#print("        fileTitle: ", fileTitle)
				totalAppearances += len(fileDict[fileTitle])
	
	#Final Print loop Statement Below:
		print(f"{wordDict} ({totalAppearances}):")
		for fileDict in alphaMasterDict[wordDict]:
			for fileTitle in fileDict:
				formattedNums = formatFrequentNumbers(fileDict[fileTitle])
				print(f"	{fileTitle}: {formattedNums}")



print(listOfFiles)
listOfFiles.sort()
print(listOfFiles)

#every file is processed and added to masterDict
for file in listOfFiles:
	concord_file = open(file, 'r')
	concorded_dict = concordance(concord_file, False)
	addToMasterDict(concorded_dict, file)
	
#masterDict is alphabetized into alphaMasterDict
alphaMasterDict = {} #ess
for i in sorted (masterDict): #ess
	alphaMasterDict[i] = masterDict[i] #ess

################################
#	CALL FUNCTION
################################

finalPrint(alphaMasterDict)




