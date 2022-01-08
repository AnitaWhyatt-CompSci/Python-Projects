#react.py
#CPTS 481 Python Software Construction
#Homework #4
#Anita Whyatt


#Particle Class
class Particle:
	def __init__(self, sym, chg, massNumber):
		self.sym = sym
		self.chg = chg
		self.massNumber = massNumber
	
	def __add__(self, other):
		return( (self, other) )
		
	def __str__(self):
		return self.sym
		
	def __repr__(self):
		className = self.__class__.__name__
		return f"{className}({self.sym!r}, {self.chg!r}, {self.massNumber!r})"


#Nucleus Class inherits from particle class
class Nucleus(Particle):
	def __str__(self):
		return f"({self.massNumber}){self.sym}"

#Our Exceptions of charge and mass balance issues
class UnbalancedCharge(Exception):
	def __init__(self, diff):
		self.diff = diff
		
	def __str__(self):
		return f"Charges are not balanced! \nThere is a difference of {self.diff} between them."

class UnbalancedNumber(Exception):
	def __init__(self, diff):
			self.diff = diff

	def __str__(self):
		return f"Mass numbers are not balanced! \nThere is a difference of {self.diff} between them."

#some functions called by classes
def createReactionString(leftTuple, rightTuple):
	returnReaction = ""
	lTupLen = len(leftTuple)
	rTupLen = len(rightTuple)
	i = 0
	for item in leftTuple:
		returnReaction += str(item)
		if i != (lTupLen - 1):
			returnReaction += " + "
		i += 1
	returnReaction += " -> "
	i = 0
	for item in rightTuple:
		returnReaction += str(item)
		if i != (rTupLen - 1):
			returnReaction += " + "
		i += 1
	#Finally, return the reaction string
	return(returnReaction)

def removeMatchingItems(leftList, rightList):
	lenLeft = len(leftList)
	lenRight = len(rightList)
	i = 0
	while i < lenLeft:
		item = leftList[i]
		if item in rightList:
			leftList.remove(item)
			rightList.remove(item)
	

	
#Reaction class, for handling reactions
class Reaction:
	def __init__(self, leftTuple, rightTuple):
		self.leftTuple = leftTuple
		self.rightTuple = rightTuple
		#Potentially raise exceptions, first get chg and mass totals
		leftChgTotal = 0
		rightChgTotal = 0
		leftMassTotal = 0
		rightMassTotal = 0
		for item in self.leftTuple:
			leftChgTotal += item.chg
			leftMassTotal += item.massNumber
		for item in self.rightTuple:
			rightChgTotal += item.chg
			rightMassTotal += item.massNumber
		#raise any necessary exceptions
		if leftChgTotal != rightChgTotal:
			absoluteDiff = abs(leftChgTotal - rightChgTotal)
			raise UnbalancedCharge(absoluteDiff)
		if leftMassTotal != rightMassTotal:
			absoluteDiff = abs(leftMassTotal - rightMassTotal)
			raise UnbalancedNumber(absoluteDiff)
	
	def __str__(self):
		return(createReactionString(self.leftTuple, self.rightTuple))


class ChainReaction:
	def __init__(self, name): #takes the name of the ChainReaction
		self.name = name
		self.reacList = []

	def addReaction(self, *addReac):
		for item in addReac:
			self.reacList += addReac
	
	def __str__(self):
		returnStr = f"{self.name}\n"
		for item in self.reacList:
			returnStr += f"{item}\n"
		#code for creating the "net" reaction
		lhsNet = []
		rhsNet = []
		for tupleItem in self.reacList:
			for item in tupleItem.leftTuple:
				lhsNet.append(item)
			for item in tupleItem.rightTuple:
				rhsNet.append(item)
		#if a particle is in lhsNet and rhsNet remove it
		lenLeft = len(lhsNet)
		lenRight = len(rhsNet)
		i = 0
		while i < lenLeft:
			item = lhsNet[i]
			i += 1
			if item in rhsNet:
				lhsNet.remove(item)
				rhsNet.remove(item)
				i = 0
			lenLeft = len(lhsNet)
			lenRight = len(rhsNet)
		
		#add to returnStr
		returnStr += "net: \n"
		returnStr += createReactionString(lhsNet, rhsNet)
		return(returnStr)
		

if __name__ == "__main__":
	print("\n**********************************\nWelcome to react.py self-test!!!")
	#declarations: Particle		
	em = Particle("e-", -1, 0)
	ep = Particle("e+", 1, 0)
	p = Particle("p", 1, 1)
	n = Particle("n", 0, 1)
	nu_e = Particle("nu_e", 0, 0)
	gamma = Particle("gamma", 0, 0)
	#declarations: Nucleus
	d = Nucleus("H", 1, 2)	
	li6 = Nucleus("Li", 3, 6)
	he4 = Nucleus("He", 2, 4)
	he3 = Nucleus("He", 2, 3)
	
	#Print off out particles and nucleus values
	print("\nAll Our Particles")
	print(em, ep, p, n, nu_e, gamma)
	print("\nAll Our Nucleuses")
	print(d, li6, he4, he3)
	print("\n")
	
	print("INPUT:")
	print("Reaction((li6, d), (he4, he4))")
	print("RESULT:")
	print(Reaction((li6, d), (he4, he4)))
	print("\n")
	print("INPUT:")
	print("Reaction(li6 + d), (he4 + he4))")
	print("RESULT:")
	print(Reaction((li6 + d), (he4 + he4)))
	
	print("\n\nINPUT:")
	print(
	"""
	chainTest = ChainReaction("proton-proton (branch I)")
	chainTest.addReaction(Reaction((p, p), (d, ep, nu_e))) 
	chainTest.addReaction(Reaction((p, p), (d, ep, nu_e)))
	chainTest.addReaction(Reaction((d, p), (he3, gamma)))
	chainTest.addReaction(Reaction((d, p), (he3, gamma)))
	chainTest.addReaction(Reaction((he3, he3), (he4, p, p)))
	"""
	)
	print("RESULT:")
	chainTest = ChainReaction("proton-proton (branch I)")
	chainTest.addReaction(Reaction((p, p), (d, ep, nu_e))) 
	chainTest.addReaction(Reaction((p, p), (d, ep, nu_e)))
	chainTest.addReaction(Reaction((d, p), (he3, gamma)))
	chainTest.addReaction(Reaction((d, p), (he3, gamma)))
	chainTest.addReaction(Reaction((he3, he3), (he4, p, p)))
	print(chainTest)
	print("\nFinally lets test our exceptions")
	print("INPUT:")
	print("Reaction((p, d, ep), (nu_e,))")
	print(Reaction((p, d, ep), (nu_e,)))











