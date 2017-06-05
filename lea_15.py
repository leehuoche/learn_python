class lister:
	def __repr__(self):
		return('intance of %s,address %s:\n%s'  %(self.__class__.__name__, id(self), self.attrnames() ))
	def attrnames(self):
		result=''
		for attr in self.__dict__.keys():
			if attr[:2]=='__':
				result+='\t name %s=built-in '%attr
			else:
				result+='\t name %s=%s\n'%(attr,self.__dict__[attr])
		return result

class super:
	def __init__(self):
		self.data1='spamm'



class sub(super,lister):
	def __init__(self):
		super.__init__(self)
		self.data2='eggs'
if __name__ == '__main__':
	x=sub()
	print x