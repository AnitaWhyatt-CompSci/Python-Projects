#Cpts 481 Python Software
#Professor: Robert Lewis
#Student: Anita Whyatt
#Homework #3 w/ Extra-Credit


class InvalidRoman(Exception):
	pass

class Roman:
	def __init__(self, val):
		if isinstance(val, int):
			if val < 2000000:
				self.val = val
			elif val >= 2000000:
				raise ValueError("Roman Numeral value may not be 2 million or greater")
		elif isinstance(val, str):
			if isLegalRoman(val) == True:
				val = convertRomanToInt(val)
				self.val = val
				#self = convertIntToRoman(val)
				#self.val = val
			else:
				raise InvalidRoman("Error: You must submit a valid roman numeral for conversion")
		#print(f"self={self}, type={type(self)}")
		#print(f"self={val}, type={type(val)}")


	###############################
	#below is _add__ and __radd__
	###############################
	
	def __add__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(convertIntToRoman(self.val + other.val))
		if isinstance(self, int)==False and isinstance(other, int)==True:
			return(convertIntToRoman(self.val + other))
		else:
			return(0)

	def __radd__(self, other): #if one of our values is an int
		if isinstance(other, int):
			return(convertIntToRoman(other + self.val))
	
	#############################################################
	#notes about sub and rsub:
	#if given the argument (IV - I) sub is called wiht self=IV and other=I
	#if given an argument (IV - 1) sub is called with self=IV other=1
	#if given (4 - I) rsub is called with self=I and other=4 ?????????
	#############################################################	
	
	def __sub__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(convertIntToRoman(self.val - other.val))
		if isinstance(self, int)==False and isinstance(other, int)==True:
			return(convertIntToRoman(self.val - other))
		else:
			return(0)
			
	def __rsub__(self, other):
		if isinstance(other, int):
			return(convertIntToRoman(other - self.val))
			
	###########################################
	#Notes on __mul__ and __rmul__
	#(III * V) calls mul with self=III and other=V
	#(3 * V) calls rmul with self=V and other=3
	#(III * 5) calls mul with self=III and other=5
	###########################################
	
	def __mul__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(convertIntToRoman(self.val * other.val))
		if isinstance(self, int)==False and isinstance(other, int)==True:
			return(convertIntToRoman(self.val * other))
		else:
			return(0)
	
	def __rmul__(self, other):
		if isinstance(other, int):
			return(convertIntToRoman(other * self.val))
	
	############################################
	#Notes on __truediv and __rtruediv__
	#(IX / II) truediv with self=IX and other=II
	#(9 / II)  rtruediv with self=II and other=9
	#(IX / 2)  truediv with self=IX and other=2
	############################################
	def __truediv__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return( (convertIntToRoman(self.val // other.val)), (convertIntToRoman(self.val % other.val)) )
		if isinstance(self, int)==False and isinstance(other, int)==True:
			return( (convertIntToRoman(self.val // other)), (convertIntToRoman(self.val % other)) )
		else:
			return(0)
	
	def __rtruediv__(self, other):
		if isinstance(other, int):
			return( (convertIntToRoman(other // self.val)), (convertIntToRoman(other % self.val)) )
	
	################################################
	#Notes on __floordiv__ and __rfloordiv__
	#(IX / II) floordiv with self=IX and other=II
	#(9 / II)  rfloordiv with self=II and other=9
	#(IX / 2)  floordiv with self=IX and other=2
	#################################################
	
	def __floordiv__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(convertIntToRoman(self.val // other.val))
		if isinstance(self, int)==False and isinstance(other, int)==True:
			return(convertIntToRoman(self.val // other))
		else:
			return(0)
	
	def __rfloordiv__(self, other):
		if isinstance(other, int):
			return(convertIntToRoman(other // self.val))
	
	#######################################################
	#Notes on __pow__ and __rpow__
	#(III ** II) calls pow with self=III and other=II
	#(3 ** II) calls rpow with self=3 and other=II
	#(III ** 2) calls mul with self=III and other=2
	
	def __pow__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(convertIntToRoman(self.val ** other.val))
		if isinstance(self, int)==False and isinstance(other, int)==True:
			return(convertIntToRoman(self.val ** other))
		else:
			return(0)
	
	def __rpow__(self, other):
		if isinstance(other, int):
			return(convertIntToRoman(other ** self.val))
	
	###############################################
	#Below is __eq__ or == operator
	
	def __eq__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(self.val == other.val)
		if isinstance(self, int)==False and isinstance(other,int)==True:
			return(self.val == other)
		if isinstance(self, int)==True and isinstance(other,int)==False:
			return(self == other.val)
	
	############################################
	#Below is __ne__ or != operator
	
	def __ne__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(self.val != other.val)
		if isinstance(self, int)==False and isinstance(other,int)==True:
			return(self.val != other)
		if isinstance(self, int)==True and isinstance(other,int)==False:
			return(self != other.val)
	
	##############################################
	#Below is __lt__ or < operator
	#__lt__ has no reflection, rather __gt__ is its reflection
	
	def __lt__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(self.val < other.val)
		if isinstance(self, int)==False and isinstance(other,int)==True:
			return(self.val < other)


	##################################################
	#Below is __gt__ or > operator
	#__gt__ has no reflection, rather__lt__ is its reflection
	
	def __gt__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(self.val > other.val)
		if isinstance(self, int)==False and isinstance(other,int)==True:
			return(self.val > other)
	
	##############################################
	#Below is __le__ or <= operator
	#__le__ has no reflection, rather __ge__ is its reflection
	
	def __le__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(self.val <= other.val)
		if isinstance(self, int)==False and isinstance(other,int)==True:
			return(self.val <= other)
	
	##############################################
	#Below is __ge__ or >= operator
	#__ge__ has no reflection, rather __le__ is its reflection
	
	def __ge__(self, other):
		if isinstance(self, int)==False and isinstance(other, int)==False:
			return(self.val >= other.val)
		if isinstance(self, int)==False and isinstance(other,int)==True:
			return(self.val >= other)
	
	#############################################
	#Below is __pos__ and __neg__ and __str__ methods
	
	def __pos__(self):
		return(convertIntToRoman(1 * self.val))
		
	def __neg__(self):
		return(convertIntToRoman(-1 * self.val))
	
	def __str__(self): #helps with print(V) = V
		return(convertIntToRomanString(self.val))
	
	def __repr__(self):
		return(f"Roman('{self}')")






def oneNumeralToInt(numeral): #Takes a single charachter and returns its int value
	if numeral == "I" or numeral == "i":
		return(1)
	elif numeral == "V" or numeral == "v":
		return(5)
	elif numeral == "X" or numeral == "x":
		return(10)
	elif numeral == "L" or numeral == "l":
		return(50)
	elif numeral == "C" or numeral == "c":
		return(100)
	elif numeral == "D" or numeral == "d":
		return(500)
	elif numeral == "M" or numeral == "m":
		return(1000)
	elif numeral == "N" or numeral == "n":
		return(0)
	else:
		print(f"Error inside oneNumeralToInt! No translation for charachter {numeral}")
		return(0)



def convertRomanToInt(romanString): #Takes a string that is a roman numeral and returns its int value
	numPositivity = 1 #-1 if number is negative
	if romanString[0] == "-": #if our string is negative
		numPositivity = -1
		romanString = romanString[1:]
	
	length = len(romanString)
	if length == 1: #if we get a single charachter just return its value quickly with no looping
		return(numPositivity * oneNumeralToInt(romanString))
		
	totalValue = 0
	previousValue = 0
	currentValue = 0
	i = 0 #counter for while loop
	while i < length:
		#first logic for (X) type cases
		if romanString[i] == "(":
			i += 1 #move into letter
			currentValue = oneNumeralToInt(romanString[i])
			currentValue = currentValue * 1000
			i += 1 #move into last parenthesis
		else:
			currentValue = oneNumeralToInt(romanString[i])
		#Now logic for adding values to total
		#print(f"(SOL) previousValue: {previousValue} currentValue: {currentValue} Total: {totalValue} ")
		if previousValue < currentValue and previousValue != 0: 
			totalValue += (currentValue - previousValue)
			#print(f"	...Adding {currentValue} - {previousValue}")
			previousValue = 0
		else:
			totalValue += previousValue
			#print(f"	...Adding {previousValue}")
			if i == (length - 1): #if this is the last iteration of the loop, add current value too
				totalValue += currentValue
				#print(f"	...Adding {currentValue}")
			previousValue = currentValue
		
		#print(f"(EOL) previousValue: {previousValue} currentValue: {currentValue} Total: {totalValue} \n")
		i += 1
			
	return(numPositivity * totalValue)	



#below used in __str__ and instantiation loop
def convertIntToRomanString(convertInt): #Special function to return str type from int
	finalRoman = ""
	if convertInt == 0: #special case for 0 int
		return("N")
	if convertInt < 0:
		finalRoman += "-"
		convertInt = convertInt * -1
	
	while convertInt > 0:
		if convertInt >= 1000000:
			finalRoman += "(M)"
			convertInt -= 1000000
		elif convertInt >= 900000:
			finalRoman += "(C)(M)"
			convertInt -= 900000
		elif convertInt >= 500000:
			finalRoman += "(D)"
			convertInt -= 500000
		elif convertInt >= 400000:
			finalRoman += "(C)(D)"
			convertInt -= 400000
		elif convertInt >= 100000:
			finalRoman += "(C)"
			convertInt -= 100000
		elif convertInt >= 90000:
			finalRoman += "(X)(C)"
			convertInt -= 90000
		elif convertInt >= 50000:
			finalRoman += "(L)"
			convertInt -= 50000
		elif convertInt >= 40000:
			finalRoman += "(X)(L)"
			convertInt -= 40000
		elif convertInt >= 10000:
			finalRoman += "(X)"
			convertInt -= 10000
		elif convertInt >= 9000:
			finalRoman += "M(X)"
			convertInt -= 9000
		elif convertInt >= 5000:
			finalRoman += "(V)"
			convertInt -= 5000
		elif convertInt >= 4000:
			finalRoman += "M(V)"
			convertInt -= 4000
		elif convertInt >= 1000:
			finalRoman += "M"
			convertInt -= 1000
		elif convertInt >= 900:
			finalRoman += "CM"
			convertInt -= 900
		elif convertInt >= 500:
			finalRoman += "D"
			convertInt -= 500
		elif convertInt >= 400:
			finalRoman += "CD"
			convertInt -= 400
		elif convertInt >= 100:
			finalRoman += "C"
			convertInt -= 100
		elif convertInt >= 90:
			finalRoman += "XC"
			convertInt -= 90
		elif convertInt >= 50:
			finalRoman += "L"
			convertInt -= 50
		elif convertInt >= 40:
			finalRoman += "XL"
			convertInt -= 40
		elif convertInt >= 10:
			finalRoman += "X"
			convertInt -= 10
		elif convertInt >= 9:
			finalRoman += "IX"
			convertInt -= 9
		elif convertInt >= 5:
			finalRoman += "V"
			convertInt -= 5
		elif convertInt >= 4:
			finalRoman += "IV"
			convertInt -= 4
		elif convertInt >= 1:
			finalRoman += "I"
			convertInt -= 1
	return(finalRoman)



def okayLegalPairs(prev, curr): #used by isLegalRoman
	if (prev == "(C)" or prev == "(c)") and (curr == "(M)" or curr == '(m)'):
		return True
	elif (prev == "(C)" or prev == "(c)") and (curr == "(D)" or curr == '(d)'):
		return True
	elif (prev == "(X)" or prev == "(x)") and (curr == "(C)" or curr == '(c)'):
		return True
	elif (prev == "(X)" or prev == "(x)") and (curr == "(L)" or curr == '(l)'):
		return True
	elif (prev == "M" or prev == "m") and (curr == "(X)" or curr == '(x)'):
		return True
	elif (prev == "M" or prev == "m") and (curr == "(V)" or curr == '(v)'):
		return True
	elif (prev == "C" or prev == "c") and (curr == "M" or curr == 'm'):
		return True
	elif (prev == "C" or prev == "c") and (curr == "D" or curr == 'd'):
		return True
	elif (prev == "X" or prev == "x") and (curr == "C" or curr == 'c'):
		return True
	elif (prev == "X" or prev == "x") and (curr == "L" or curr == 'l'):
		return True
	elif (prev == "I" or prev == "i") and (curr == "X" or curr == 'x'):
		return True
	elif (prev == "I" or prev == "i") and (curr == "V" or curr == 'v'):
		return True
	else:
		return False


	
#Fuction to discover if string is legal roman numeral
def isLegalRoman(maybeRomanString):
	allowedChars = "IVXLCDM()ivxlcdm"
	length = len(maybeRomanString)
	if maybeRomanString[0] == "-":
		maybeRomanString = maybeRomanString[1:]
		if maybeRomanString == "":
			return False
	
	if len == 1 and maybeRomanString[0] in allowedChars:
		return True
	elif len == 1 and maybeRomanString[0] not in allowedChars:
		return False
	
	currentChar = ""
	previousChar = ""
	i = 0
	while i < length:
		currentChar = maybeRomanString[i]
		if currentChar not in allowedChars:
			return False
		
		if currentChar == "(":
			if (i+2) < length and (maybeRomanString[i+1] in allowedChars) and maybeRomanString[i+2] == ")":
				currentChar = f"({maybeRomanString[i+1]})"
				i += 2
			else:
				return False
		
		if previousChar != "" and convertRomanToInt(previousChar) < convertRomanToInt(currentChar):
			if okayLegalPairs(previousChar, currentChar) == False:
				return False
		
		previousChar = currentChar
		i += 1
		if i == length:
			return True
			
	
	
def convertIntToRoman(startInt): #Takes an int and converts it to roman string
	finalRoman = ""
	convertInt = startInt
	if convertInt == 0: #special case for 0 int
		return("N")
	if convertInt < 0:
		finalRoman += "-"
		convertInt = convertInt * -1
	
	while convertInt > 0:
		if convertInt >= 1000000:
			finalRoman += "(M)"
			convertInt -= 1000000
		elif convertInt >= 900000:
			finalRoman += "(C)(M)"
			convertInt -= 900000
		elif convertInt >= 500000:
			finalRoman += "(D)"
			convertInt -= 500000
		elif convertInt >= 400000:
			finalRoman += "(C)(D)"
			convertInt -= 400000
		elif convertInt >= 100000:
			finalRoman += "(C)"
			convertInt -= 100000
		elif convertInt >= 90000:
			finalRoman += "(X)(C)"
			convertInt -= 90000
		elif convertInt >= 50000:
			finalRoman += "(L)"
			convertInt -= 50000
		elif convertInt >= 40000:
			finalRoman += "(X)(L)"
			convertInt -= 40000
		elif convertInt >= 10000:
			finalRoman += "(X)"
			convertInt -= 10000
		elif convertInt >= 9000:
			finalRoman += "M(X)"
			convertInt -= 9000
		elif convertInt >= 5000:
			finalRoman += "(V)"
			convertInt -= 5000
		elif convertInt >= 4000:
			finalRoman += "M(V)"
			convertInt -= 4000
		elif convertInt >= 1000:
			finalRoman += "M"
			convertInt -= 1000
		elif convertInt >= 900:
			finalRoman += "CM"
			convertInt -= 900
		elif convertInt >= 500:
			finalRoman += "D"
			convertInt -= 500
		elif convertInt >= 400:
			finalRoman += "CD"
			convertInt -= 400
		elif convertInt >= 100:
			finalRoman += "C"
			convertInt -= 100
		elif convertInt >= 90:
			finalRoman += "XC"
			convertInt -= 90
		elif convertInt >= 50:
			finalRoman += "L"
			convertInt -= 50
		elif convertInt >= 40:
			finalRoman += "XL"
			convertInt -= 40
		elif convertInt >= 10:
			finalRoman += "X"
			convertInt -= 10
		elif convertInt >= 9:
			finalRoman += "IX"
			convertInt -= 9
		elif convertInt >= 5:
			finalRoman += "V"
			convertInt -= 5
		elif convertInt >= 4:
			finalRoman += "IV"
			convertInt -= 4
		elif convertInt >= 1:
			finalRoman += "I"
			convertInt -= 1
	if finalRoman in globals(): #if variable already exist, return it!
		returnRoman = globals()[finalRoman]
		return(returnRoman)
	else: #if variable doesn't exist, make it exist!
		globals()[finalRoman] = Roman(startInt)
		return( (globals()[finalRoman]) )



# Instantiate Romans from -1000 to 1000
iVal = -1000
while iVal <= 1000:
	rVal = convertIntToRomanString(iVal)
	globals()[rVal] = Roman(iVal)
	iVal += 1

#EXTRA-CREDIT TEST CASE:
#print(Roman('MM'))
#MM		#returns prior























