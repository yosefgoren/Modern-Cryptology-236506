def decide(N: int, M: int, factoring_oracle)->bool:
	"""returns 'True' if (N,M) is in L, and False otherwise."""
	prime_factors = factoring_oracle(N)
	return max(prime_factors) > M