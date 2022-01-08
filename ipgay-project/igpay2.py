#igpay2.py
#CPTS 481 Python Software Construction
#Homework #1
#Anita Whyatt

#This is the "enhanced" igpay file called for in problem 2 of the homework
#This code will take a word, of any casing and return it in piglatin, while also
#ensuring its "casing" remains as part of one of three types


vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def igpay2(input):
	ct = "" #ct = case_type
	if len(input) != 1:
		if input[0] in lower_case and input[1] in lower_case:
			#print("ct = 'lower' ")
			ct = "lower"
		elif input[0] in upper_case and input[1] in upper_case:
			#print("ct = 'UPPER' ")
			ct = "UPPER"
		elif input[0] in upper_case and input[1] in lower_case:
			#print("ct = 'Capital' ")
			ct = "Capital"
	else:
		#print("input length is 1")
		if input[0] in lower_case:
			#print("ct = 'lower' ")
			ct = "lower"
		elif input[0] in upper_case:
			#print("ct = 'UPPER' ")
			ct = "UPPER"
	inputed_word = input.lower() #we will handle the word in all lower case, then change it right before it is returned
	move_to_back = ""
	word_length = len(inputed_word)
	if inputed_word[0] in vowels: #return(inputed_word + "way")
		#return loop below
		if ct == "lower":
			return(inputed_word + "way")
		elif ct == "UPPER":
			return(inputed_word.upper() + "WAY")
		elif ct == "Capital":
			return(inputed_word.capitalize() + "way")	
	counter = 0
	while counter < word_length:
		#print(f"****************** \n OUR INPUT_WORD IS: {inputed_word}")
		#print(f"loop {counter} of {word_length}, letter={inputed_word[0]}, move_to_back = {move_to_back}")
		#above print tests what program is seeing
		if inputed_word[0] in consonants:
			#print(f"{inputed_word[0]} is consonant")
			move_to_back = move_to_back + inputed_word[0]
			#print(f"our inputed_word before slice is {inputed_word} input={input}, move_to_back={move_to_back}")
			inputed_word = inputed_word[1:]
			if input.lower() == move_to_back:
				#return loop below
				if ct == "lower":
					return input
				elif ct == "UPPER":
					return input.upper()
				elif ct == "Capital":
					return input.capitalize()
				#inputed_word = inputed_word[1:] #original slice location
		if inputed_word[0] in vowels: 
			if ct == "lower": #return loop begin
				return(inputed_word + move_to_back + "ay")
			elif ct == "UPPER":
				return(inputed_word.upper() + move_to_back.upper() + "AY")
			elif ct == "Capital":
				return(inputed_word.capitalize() + move_to_back + "ay")
		counter +=1
		
		
if __name__ == "__main__":
	print("Let's run a suite of test cases!")
	print("*************** \n Word:   pig")
	print("Result: ", igpay2("pig"))
	print("*************** \n Word:   Pig")
	print("Result: ", igpay2("Pig"))
	print("*************** \n Word:   PIG")
	print("Result: ", igpay2("PIG"))
	
	print("*************** \n Word:   latin")
	print("Result: ", igpay2("latin"))
	print("*************** \n Word:   Latin")
	print("Result: ", igpay2("Latin"))
	print("*************** \n Word:   LATIN")
	print("Result: ", igpay2("LATIN"))
	
	print("*************** \n Word:   happy")
	print("Result: ", igpay2("happy"))
	print("*************** \n Word:   Happy")
	print("Result: ", igpay2("Happy"))
	print("*************** \n Word:   HAPPY")
	print("Result: ", igpay2("HAPPY"))
	
	print("*************** \n Word:   glove")
	print("Result: ", igpay2("glove"))
	print("*************** \n Word:   Glove")
	print("Result: ", igpay2("Glove"))
	print("*************** \n Word:   GLOVE")
	print("Result: ", igpay2("GLOVE"))
	
	print("*************** \n Word:   stove")
	print("Result: ", igpay2("stove"))
	print("*************** \n Word:   Stove")
	print("Result: ", igpay2("Stove"))
	print("*************** \n Word:   STOVE")
	print("Result: ", igpay2("STOVE"))
	
	print("*************** \n Word:   knights")
	print("Result: ", igpay2("knights"))
	print("*************** \n Word:   Knights")
	print("Result: ", igpay2("Knights"))
	print("*************** \n Word:   KNIGHTS")
	print("Result: ", igpay2("KNIGHTS"))
	
	print("*************** \n Word:   alabaster")
	print("Result: ", igpay2("alabaster"))
	print("*************** \n Word:   Alabaster")
	print("Result: ", igpay2("Alabaster"))
	print("*************** \n Word:   ALABASTER")
	print("Result: ", igpay2("ALABASTER"))
	
	print("*************** \n Word:   omelet")
	print("Result: ", igpay2("omelet"))
	print("*************** \n Word:   Omelet")
	print("Result: ", igpay2("Omelet"))
	print("*************** \n Word:   OMELET")
	print("Result: ", igpay2("OMELET"))
	
	print("*************** \n Word:   applepie")
	print("Result: ", igpay2("applepie"))
	print("*************** \n Word:   Applepie")
	print("Result: ", igpay2("Applepie"))
	print("*************** \n Word:   APPLEPIE")
	print("Result: ", igpay2("APPLEPIE"))
	
	print("*************** \n Word:   i")
	print("Result: ", igpay2("i"))
	print("*************** \n Word:   I")
	print("Result: ", igpay2("I"))
	
	print("*************** \n Word:   cry")
	print("Result: ", igpay2("cry"))
	print("*************** \n Word:   Cry")
	print("Result: ", igpay2("Cry"))
	print("*************** \n Word:   CRY")
	print("Result: ", igpay2("CRY"))
	
	print("*************** \n Word:   why")
	print("Result: ", igpay2("why"))
	print("*************** \n Word:   Why")
	print("Result: ", igpay2("Why"))
	print("*************** \n Word:   WHY")
	print("Result: ", igpay2("WHY"))
		
	
#print_out = igpay2("monkey")
#print(print_out)





