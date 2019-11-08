class adder:
	def __init__(self,value=0):
		self.data=value
	def __add__(self,other):
		self.data+=other
class addrepr(adder):
	def __repr__(self):
		return 'addrepr(%s)'%self.data

x=addrepr(2)
print x
x+1
print x
