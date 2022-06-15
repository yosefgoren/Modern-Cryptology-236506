from code.q3_decide import *

def bruteforce(N: int)->tuple:
	factors = []
	while N > 1:
		#find another factor:
		for i in range(2, N+1):#when there are no factors, i = N at the end.
			if (N%i) == 0:
				factors.append(i)
				N = N//i
				break
	return factors[::-1]

def print_partial(factors: list):
	total = 1
	for f in factors:
		total = total*f
		print(f, total)


def test_decomp():
	N = 32
	print("control")
	print_partial(bruteforce(N))
	decide_oracle = lambda N,M: decide(N, M, bruteforce)
	print("test")
	print_partial(factor(N, decide_oracle))
	

	

	


if __name__ == "__main__":
	test_decomp()