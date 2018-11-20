def primeNumbers(number):
	data_type = (list, dict)

	if not isinstance(number, data_type):
		prime_numbers = []
		if number > 0:
			for x in range(2, number + 1):
				isprime = True
				for y in range(2, x):
					if x % y == 0:
						isprime = False
						break
				if isprime:
					prime_numbers.append(x)
		# else:
		# 	return prime_numbers
			
	else:
		raise TypeError

	return prime_numbers

print(primeNumbers(8))