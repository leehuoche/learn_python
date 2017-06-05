"""
class pp(supercalss):
	data=value
	def method(self):
		self.member=value
"""
"""		
class sharedata:
	spam=42

x=sharedata()
y=sharedata()
sharedata.spam=99
x.spam=66

print x.spam,y.spam
"""

class adder:
	def __init__(self,value=0):
		self.data=value
	def __add__(self,other):
		self.data+=other


class addrepr(adder):
	def __repr__(self):
		return 'addrepr(%s) '%self.data

x=addrepr(2)
print x+1
x
print x
print str(x),repr(x)

class addstr(adder):
	def __str__(self):
		return '[Value:%s]'%self.data

x=addstr(3)
x+1
print x
print str(x),repr(x)

class addboth(adder):
	def __str__(self):
		return '[Value:%s]'%self.data
	def __repr__(self):
		return 'addboth(%s)'%self.data

x=addboth(4)
x+1
print x
print str(x),repr(x)