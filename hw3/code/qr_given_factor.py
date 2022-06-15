def qr(a: int, P: int, Q: int)->bool:
	"""the algorithm determines if 'x' is
		quadratic residue of under modulus PQ"""
	a_is_P_qr = a**((P-1)/2)%P == 1
	a_is_Q_qr = a**((Q-1)/2)%Q == 1
	return a_is_P_qr and a_is_Q_qr