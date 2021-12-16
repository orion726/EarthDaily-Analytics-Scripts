"""
This script calculates the nth number in the Fibonacci sequence
[0, 1, 1, 2, 3, 5...] where F_n = F_(n-1) + F_(n-2).

There are 3 functions:

	fibonacci_n - This calculates the nth elementh of the 
		Fibonacci sequence with a for loop. This is runs 
		in O(n) time.

	fibonacci_closed_form1 - This calculates the nth element
		of the Fibonacci seuence without loops or any recursion.
		This approach is only accurate for n<=70, but is better
		than O(n) time.

	fibonacci_closed_form2 - This calculates the nth element
		of the Fibonacci seuence without loops or any recursion, 
		but allows for arbitrily large values of n. This approach 
		is much slower than O(n) time.

	Input:
		num - element of Fibonacci sequence required, int

	Output:
		fib - nth number of Fibonacci sequence as calculated by
			each function

	Dependencies:
		math
		decimal
	
"""

import math as m
import decimal as d

def fibonacci_n(n):
	"""
	This function returns the nth number in the Fibonacci sequence
	[0, 1, 1, 2, 3, 5...] where F_n = F_(n-1) + F_(n-2).

	Input:
		n - element of Fibonacci sequence required

	Output:

		fib - nth number of Fibonacci sequence, int
	"""
	# First 2 values of Fibonacci sequence are [0,1]

	if n <= 1:
		return n

	previous = 0
	current  = 1

	# Loop over indicies up to n-1 calculating the previous and
	# current Fibonacci values

	for _ in range(n - 1):
		previous, current = current, previous + current

	# Return the last "cuurent" variable, which is the nth value
	# of the Fibonacci sequence

	return current

def fibonacci_closed_form1(n):
	"""
	This function estimates the nth number in the Fibonacci sequence
	[0, 1, 1, 2, 3, 5...] where F_n = F_(n-1) + F_(n-2). This function
	avoids using recursion, for loops, or while loops by adopting the 
	closed form of the sequence:

	F_n = 1/sqrt(5) * ((0.5*(1 + sqrt(5)))**n - (0.5*(1 - sqrt(5)))**n)

	Input:
		n - element of Fibonacci sequence required

	Output:
		fib - nth number of Fibonacci sequence, int

	Dependencies:
		math

	This solution will only be accurate for n<=70, assuming the code is
	ran on a 64-bit system. 
	"""

	# Closed form of the Fibonacci sequence

	F = 1/m.sqrt(5) * ( (0.5*(1+m.sqrt(5)))**n - (0.5*(1-m.sqrt(5)))**n )

	# Return the rounded value to get ride of extra decimal place(s)

	return round(F)

def fibonacci_closed_form2(n):
	"""
	This function estimates the nth number in the Fibonacci sequence
	[0, 1, 1, 2, 3, 5...] where F_n = F_(n-1) + F_(n-2). This function
	avoids using recursion by adopting the closed form of the sequence:

	F_n = (f^n - (-f)^-n) / (2f-1)

	where f = (1 + 5^0.5) / 2

	This will result in an approximation only as accurate as the estimate 
	for 5^0.5. The level of precision is adjusted to include an increasing 
	number of decimal places based on n.

	Input:

		n - element of Fibonacci sequence required

	Output:

		fib - nth number of Fibonacci sequence, int

	Dependencies:
		
		decimal

	"""


	n = int(n)

	# Set the level of precision
	
	if n <= 30:
		d.getcontext().prec = int(7)
	else:
		d.getcontext().prec = int(n/4)
	
	# Estimate of sqrt(5) to decimal precision a/4

	f = d.Decimal(0.5) * ( d.Decimal(1) + d.Decimal(5) ** d.Decimal('0.5'))

	# Calculate the closed form of the fibonacci sequence

	fib = (f**d.Decimal(n) - (-f)**d.Decimal(-n)) / (2*f -1)

	# Return the rounded value to get ride of extra decimal places	

	return round(fib)





# nth Value of the Fibonacci sequence to be calculated
	
num = 25

print("Comparisons: \n")

print("Closed Form, Estimator")
print(fibonacci_closed_form1(num))

print("Closed Form, Percise")
print(fibonacci_closed_form2(num))

print("For Loop")
print(fibonacci_n(num))

