class empty:
	def __getattr__(self,attrname):
		if attrname=='age':
			return 40
		else:
			raise AttributeError, attrname

x=empty()
print x.name