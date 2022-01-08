#Cpts 481 Python Software
#Homework #2 Problem #1
#Student: Anita Whyatt

import sys #import sys for sys.argv
filename = sys.argv[-1]


#stripPunc is seperate function we will call to strip words
#	of punctuation at start and end, accepts any casing and
#	always returns lower case.
def stripPunc(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	word = word.lower()
	while True:
		if len(word) == 0:
			return ""
		if word[0] not in alphabet:
			word = word[1:]
		elif word[-1] not in alphabet:
			word = word[:-1]
		else:
			return word




#this function takes an open file of text and returns a
#	"concordance" of its contents. Because it takes an open
#	file, both opening and closing are expected to be
#handled externally

def concordance(f, unique=True):
	opened_file = f
	opened_file.seek(0, 0) #set cursor to start of file
	concordanceDict = {}
	for current_line, line in enumerate(opened_file):
		line_list = line.split()
		for word in line_list:
			word = stripPunc(word)
			if word in concordanceDict:
				if unique == True:
					if (current_line + 1) not in concordanceDict[word]:
						concordanceDict[word].append(current_line + 1)
				elif unique == False: 
					concordanceDict[word].append(current_line + 1)
			if word not in concordanceDict:
				concordanceDict[word] = [current_line + 1]
	#opened_file.close() #should this function handle closing, or do externally???
	return(concordanceDict)		
	




if __name__ == "__main__":
	colors_test_file = open("colors.txt", 'r')
	print("\n\n*****************************************\nTestcase For colors.txt with unique=True\n")
	print(concordance(colors_test_file, True))
	print("\n\n*****************************************\nTestcase For colors.txt with unique=False\n")
	print(concordance(colors_test_file, False))
	colors_test_file.close()
	
	fruit_test_file = open("fruit.txt", 'r')
	print("\n\n*****************************************\nTestcase For fruit.txt with unique=True\n")
	print(concordance(fruit_test_file, True))
	print("\n\n*****************************************\nTestcase For fruit.txt with unique=False\n")
	print(concordance(fruit_test_file, False))
	fruit_test_file.close()

#set cursor to beginning of file:
#colors_test_file.seek(0, 0)

























