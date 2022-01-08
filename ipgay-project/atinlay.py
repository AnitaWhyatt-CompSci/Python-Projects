#atinlay.py
#CPTS 481 Python Software Construction
#Homework #1
#Anita Whyatt

#in this file we will take in the contents of a file as a string
#pick out the word and the punctuation 
#use igpay2.py on the strings that we wish to translate
#and output a version of the user's input in piglatin

import sys #import sys for sys.argv
filename = sys.argv[-1]
#print(filename)

from igpay2 import igpay2 #import our "enhanced" version of igpay called "igpay2"

punctuation = ".,;:!?"	#consider adding other punctuation?
 

def atinlay(input_file):
	input_string = open(input_file, 'r').read()
	#print(input_string)
	#print(input_string.split())
	
	#we know we can pass string arguments to igpay2
	string1 = "cat"
	#print(igpay2(string1))
	
	space_seperated_string = ""
	for item in input_string:
		if item in punctuation:
			output_char = " %s" % item
		else:
			output_char = item
		space_seperated_string += output_char
	
	starting_list = space_seperated_string.split()
	length_starting_list = len(starting_list)
	ending_list = []
	ending_string = ""
	#print(f"starting_list={starting_list}, length_starting_list={length_starting_list} ")
	#next we create loop to iterate through starting list
	counter = 0
	while counter < length_starting_list:
		if starting_list[counter] in punctuation:
			#print(starting_list[counter])
			ending_string += starting_list[counter]
		else: #starting_list[counter].isalpha():
			#print(igpay2(starting_list[counter]))
			ending_string += ( " " + (igpay2(starting_list[counter])) )
		#else:
		#	print(f"ERROR: Unsupported charachter {starting_list[counter]} detected, skipping...\n")
		counter += 1	
	print(ending_string)


atinlay(filename)






















