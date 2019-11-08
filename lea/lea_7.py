class super:
	"""docstring for super"""
	def method(self):
		print 'in super method'

class sub(super):
	def method(self):
		print 'in sub method'
		super.method(self)
		print 'ending sub'
x=sub()
x.method()

