def getInBinary(x: int)->list:
	if x == 0:
		return [0]
	res = []
	while x > 0:
		res.append(x%2)
		x = x//2
	return res

def slowModexp(base: int, power: int, N: int)->int:
	res = 1
	for _ in range(power):
		res = (res*base)%N
	return res

def fastModexp(base:int, power: int, N: int)->int:
	power_values = [base]
	current_power = 1
	while current_power <= power:
		highest_value = power_values[-1]
		highest_value = (highest_value**2)%N
		power_values.append(highest_value)
		current_power *= 2

	result = 1
	for idx, is_value_required in enumerate(getInBinary(power)):
		if is_value_required == 1:
			result = (result*power_values[idx])%N
	return result

def main():
	print(f"{fastModexp(6, 170009564, 190)=}")
	print(f"{slowModexp(6, 170009564, 190)=}")

if __name__ == "__main__":
	main()