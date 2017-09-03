from functools import lru_cache
import sys

@lru_cache(maxsize = 1000)#This is to speed the cod




def fibonacci(n):

	# Check that the input is  a positive interger
	if type(n) != int or n < 1:
		raise TypeError("n must be a positive int")

	# Compute the Nth term

	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)
#This is the input code.
r = 0
while True:
    try:
        while (type(r) != int) or (r < 1):
            r = int(input("How many steps would you like to get to? "))
        break
    except ValueError:
        print("Your input must be a valid positive interger.")
#This prints out our Output
for n in range(1, r+1):
    print(n, ":", fibonacci(n))




