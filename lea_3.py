"""
class commuter:
	def __init__(self,val):
		self.val=val
	def __add__(self,other):
		print 'add',self.val,other
	def __radd__(self,other):
		print 'radd',self.val,other

x=commuter(88)
y=commuter(99)
x+1
1+y
x+y
"""
"""
class prod:
	def __init__(self,value):
		self.value=value
	def __call__(self,other):   #这是对于（）的重载
		return self.value*other
x=prod(2)
print x(3)
"""



