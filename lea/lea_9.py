class indexer:
	"""docstring for indexer __init__(self, arg):
		super(indexer__init__()
		selfarg = arg
	"""
	def __getitem__(self,index):
		return index**2

x=indexer()
print x[2]

class stepper:
	def __getitem__(self,i):
		return self.data[i]

x=stepper()
x.data='spam'
print x[1]

print 'm' in x