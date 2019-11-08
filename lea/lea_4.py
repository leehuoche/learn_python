class lister:
	def __repr__(self):
		return("instance of %s,address %s:\n %s"%(self.__class__.__name__,id(self),self.attrnames()) )
	def attrnames(self):
		result=''
		for attr in self.__dict__.keys():
			if attr[:2]=='__':
				result=result+"\t name%s=<built-in>\n"%attr
			else:
				result=result+"\t name%s=%s\n"%(attr,self.__dict__[attr])
		return result


class spam(lister):
	def __init__(self):
		self.data1='food'

class super:
	def __init__(self):
		self.data1='spam'

class sub(super,lister):
	def __init__(self):
		super.__init__(self)
		self.data2='eggs'
		self.data3=42

class x(lister):pass


t=x()
t.a=1; t.b=2; t.c=3
print t