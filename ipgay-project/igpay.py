#igpay.py
#CPTS 481 Python Software Construction
#Homework #1
#Anita Whyatt


#the following code assumes all input will be lower case and not an empty string
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def igpay(input):
	inputed_word = input
	move_to_back = ""
	word_length = len(inputed_word)
	if inputed_word[0] in vowels: 
		return(inputed_word + "way")
	counter = 0
	while counter < word_length:
		#print(f"****************** \n OUR INPUT_WORD IS: {inputed_word}")
		#print(f"loop {counter} of {word_length}, letter={inputed_word[0]}, move_to_back = {move_to_back}")
		#above print tests what program is seeing
		if inputed_word[0] in consonants:
			#print(f"{inputed_word[0]} is consonant")
			move_to_back = move_to_back + inputed_word[0]
			if input == move_to_back:
				return input
			else:
				inputed_word = inputed_word[1:]
			#inputed_word = inputed_word[1:] #i must remove the first charachter of the string
		if inputed_word[0] in vowels:
			#print(f"{inputed_word[0]} is vowel")
			return(inputed_word + move_to_back + "ay")
		counter +=1


if __name__ == "__main__":
	print("Let's run a suite of test cases!")
	print("*************** \n Word:   pig")
	print("Result: ", igpay("pig"))
	print("*************** \n Word:   latin")
	print("Result: ", igpay("latin"))
	print("*************** \n Word:   happy")
	print("Result: ", igpay("happy"))
	print("*************** \n Word:   glove")
	print("Result: ", igpay("glove"))
	print("*************** \n Word:   stove")
	print("Result: ", igpay("stove"))
	print("*************** \n Word:   knights")
	print("Result: ", igpay("knights"))
	print("*************** \n Word:   alabaster")
	print("Result: ", igpay("alabaster"))
	print("*************** \n Word:   omelet")
	print("Result: ", igpay("omelet"))
	print("*************** \n Word:   applepie")
	print("Result: ", igpay("applepie"))
	print("*************** \n Word:   i")
	print("Result: ", igpay("i"))
	print("*************** \n Word:   cry")
	print("Result: ", igpay("cry"))
	print("*************** \n Word:   why")
	print("Result: ", igpay("why"))

#result = igpay("monkey")
#print(result)




