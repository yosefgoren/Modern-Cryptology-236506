import qr_given_factor

def KeyGen(n, prime_generator: function)->tuple:
	"""given the security parameter 'n'.
		function 'prime_generator' generates random
		primes of length dictated by a parameter."""
	P, Q = prime_generator(n), prime_generator(n)
	private_key = (P,Q)
	public_key = P*Q #this is 'N'
	return private_key, public_key

def Encrypt(bit: bool, public_key, uniform_sampler: function):
	"""'uniform_sampler(k)' samples uniformly from {1...k}."""
	N = public_key
	root = uniform_sampler(N)
	if bit:
		return (root**2)*(-1)%N #cypher is QNR
	else:
		return (root**2)%N #cypher is QR

def Decrypt(cypher: bool, private_key)->bool:
	"""the 'qr' function used here is the one defined in
		subsection 1.1"""
	P,Q = private_key
	return not qr_given_factor.qr(cypher, P, Q)