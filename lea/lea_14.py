class wr:
	def __init__(self,object):
		self.wrapped=object
	def __getattr__(self,attrname):
		print 'trace',attrname
		return getattr(self.wrapped,attrname)

x=wr([1,2,3])
x.append(4)
print x.wrapped


