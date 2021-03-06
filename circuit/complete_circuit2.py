class LogicGate:
	"""
	Base class, interface with subclasses to perform gate logic
	"""
	def __init__(self,n):
		self.name = n
		self.output = None

	def getName(self):
		return self.name

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output


class BinaryGate(LogicGate):
	"""
	Operates on two inputs to produce one output.
	Gathers external input from user or gate.
	Sets up which pins will receive input.
	"""
	def __init__(self,n):
		LogicGate.__init__(self,n)

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
	"""
	Returns true when both inputs are true.
	"""
	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a==1 and b==1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):
	"""
	Returns true when at least one input is true.	
	"""
	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a==1 or b==1:
			return 1
		else:
			return 0

class UnaryGate(LogicGate):
	"""
	Operates one input into one output.
	"""
	def __init__(self,n):
		LogicGate.__init__(self,n)

		self.pin = None

	def getPin(self):
		if self.pin == None:
			return int(input("Enter Pin input for gate "+self.getName()+"-->"))
		else:
			return self.pin.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pin == None:
			self.pin = source
		else:
			print("Cannot Connect: NO EMPTY PINS on this gate")

class BufferGate(UnaryGate):
	"""
	Produces same output as input
	"""
	def __init__(self,n):
		UnaryGate.__init__(self,n)

	def performGateLogic(self):
		if self.getPin():
			return 1
		else:
			return 0

class NotGate(UnaryGate):
	"""
	Negates one input to it's opposite
	"""
	def __init__(self,n):
		UnaryGate.__init__(self,n)

	def performGateLogic(self):
		if self.getPin():
			return 0
		else:
			return 1


class Connector:
	"""
	Used to compose I/O between each gate, only uses gate-to-gate interfacing.
	Possibly modify to interface I/O directly.
	"""
	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate

class NandGate(BinaryGate):
	"""
	Returns false when both inputs are true.
	"""
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a==1 and b==1:
			return 0
		else:
			return 1

class NorGate(BinaryGate):
	"""
	Returns false when either inputs are true.
	"""
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a==1 or b==1:
			return 0
		else:
			return 1

class XorGate(BinaryGate):
	"""
	Returns true when only one of two inputs are true, otherwise false.
	"""
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a==1 and b==1:
			return 0
		elif a==0 and b==0:
			return 0
		else:
			return 1

class XnorGate(BinaryGate):
	"""
	Returns false when only one of two inputs are true, otherwise true.
	"""
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a==1 and b==1:
			return 1
		elif a==0 and b==0:
			return 1
		else:
			return 0

# Call the any of the following to test...
#  NOT (( A and B) or (C and D)) == NOT( A and B ) and NOT (C and D)
def circuit1():
	#  NOT (( A and B) or (C and D))
	print "Circuit 1"
	g1 = AndGate("G1")
	g2 = AndGate("G2")
	g3 = OrGate("G3")
	g4 = NotGate("G4")
	c1 = Connector(g1, g3)
	c2 = Connector(g2, g3)
	c3 = Connector(g3, g4)
	result = g4.getOutput()
	return result

def circuit2():
	#  NOT( A and B ) and NOT (C and D)
	print "Circuit 2"
	g1 = NandGate("G1")
	g2 = NandGate("G2")
	g3 = AndGate("G3")
	c1 = Connector(g1, g3)
	c2 = Connector(g2, g3)
	result = g3.getOutput()

	return result

def GateTest():
	a = circuit1()
	print "1st: ", a
	b = circuit2()
	print "2nd: ", b


class HalfAdder(BinaryGate):	
	"""
	The most simple arithmetic circuit.
	2 inputs => 2 outputs
	"""
	def __init__(self, n):
		BinaryGate.__init__(self, n)
		self.xorOut = None
		self.andOut = None

	def performGateLogic(self):
		g1 = XorGate("G1") # how to reach (using setters? setNextPin()?)?
		g2 = AndGate("G2") # how to reach (using setters? setNextPin()?)?
		self.xorOut = g1.getOutput()
		self.andOut = g2.getOutput()

	# can connector handle strict I/O or only gates?
	def getXor(self):
		return self.xorOut

	def getAnd(self):
		return self.andOut


# Untested
class FullAdder(HalfAdder):
	"""
	Extend HalfAdder into 8-bit full-adder: AdderTest()
	3 inputs => 2 outputs
	"""
	def __init__(self, n):
		HalfAdder.__init__(self, n)
		self.sum = None
		self.carry_out = None
		self.b1 = BufferGate("B1") # get input for carry input
		self.a1 = HalfAdder("A1")
		self.a2 = HalfAdder("A2")
		self.g1 = OrGate("G1")

	#Incomplete
	def performGateLogic(self):
		a1.getOutput()        # performGateLogic sets gate output variables
		#consider making a BufferGate(UnaryGate)
		carry_in = b1.getPin()# connect to both a2(xor, and)

		a1.getXor()           # connect to both a2(xor, and)
		a1.getAnd()           # connect to g1
		a2.getXor()           # set self.sum
		a2.getAnd()           # connect to g1.carry_out

		self.carry_out = g1.getOutput() # set self.carry_out
		self.sum = a2.getXor()          # set self.sum

		# Connect where needed.
		#test this: consider modifying Connector?
		# c = Connector(b1, a2.setAnd().setPinA())
		# c = Connector(b1, a2.setXor().setPinA())
		c1 = Connector(b1,a2)
		c2 = Connector(a2,g1)
		c3 = Connector(a1,g1)


	def getSum(self):
		return self.sum

	def getCarry(self):
		return self.carry

# Incomplete
#def AdderTest()


"""
========================================================

The circuit simulation shown in this chapter works in a backward direction. 

In other words, given a circuit, 
 the output is produced by working back through the input values, 
 which in turn cause other outputs to be queried. 

This continues until external input lines are found, 
 at which point the user is asked for values. 

Modify the implementation so that the action is in the forward direction; 
 upon receiving inputs the circuit produces an output.

========================================================
"""
# consider making Setters for input, as opposed to getOutput() heirarchy
