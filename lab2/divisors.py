def numbers():
	n=int(raw_input('choose n'))
	for num in xrange(n):
		if n%(num+1)==0:
			print num
		
numbers() 



