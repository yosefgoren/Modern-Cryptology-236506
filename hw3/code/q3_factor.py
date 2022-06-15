def factor(N: int, decide_oracle)->tuple:
	"""given a number 'N',
		and given a 'decide_oracle' function which decides 'L',
		return the list of prime factors of 'N'.
		The implementations is a loop of binary searches."""
	prime_factors = []
	while N > 1:	
		#find the largest prime factor of current 'N':
		left, right = 1, N
		while left < right-1:
			M = (left+right)//2
			if decide_oracle(N, M):
				left = M
			else:
				right = M
		largest_prime_factor = right
		#add it to list and update 'N':
		prime_factors.append(largest_prime_factor)
		N = N//largest_prime_factor
	return prime_factors