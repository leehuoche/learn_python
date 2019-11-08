class prod:
	def __init__(self,value):
		self.value=value
	def __call__(self,other):
		return self.value**other

x=prod(8)
print x(2)


class life:
	"""docstring for life"""
	def __init__(self, name='unkonw'):
		print 'hello',name
		self.name=name
	def __del__(self):
		print 'goodbye',self.name


a=life('brain')
a=0b