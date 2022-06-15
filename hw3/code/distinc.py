def product(a: list, b: list)->bool:
	"""returns the product <a,b>."""
	pass

#Assuming that n = 4.
#Assuming that S = {s}:
s = [True, False, False, True]

def D(rb: list)->bool:
	"""
	The 'rb' input is a list of booleans representing a value from {0,1}^n.
	D is a distringuisher.
		If it returns true, it thinks the input is from the "r,<r,s>",
		otherwise it thinks the input is from a uniform distribution.
	"""
	r = rb[:-1]
	b = rb[-1]
	return b == product(r, s)
