
def gen(N):
	for i in range(N):
		yield i**2


g=gen(8)
print g.next()
print g.next()

print g.next()
