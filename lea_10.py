class sqr:
	"""docstring for sqr __init__(self, arg):
		super(sqr__init__()
		self.arg = arg
	"""
	def __init__(self,start,stop):
		self.value=start-1
		self.stop=stop

	def __iter__(self):
		return self
	def next(self):
		if self.value==self.stop:
			raise StopIteration
		self.value+=1
		return self.value**2

for i in sqr(1,5):
	print i,

def gsqr(start,stop):
	for i in range(start,stop):
		yield i**2


print '\n'
for i in gsqr(1,5):
	print i,