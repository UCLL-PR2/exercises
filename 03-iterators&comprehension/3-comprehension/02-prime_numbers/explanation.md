# Assignment

- Write a functione called **prime_numbers** that generates a list of all prime numbers less than 100 using list comprehension. This could be done in one line of code.


**_Hint:_**  To test whether a number is prime or not, we have to test only till floor(sqrt(n)). The list comprehension iterates over all numbers from 2 to 100 (inclusive) and checks if the number is prime. It uses the all() function along with a nested comprehension to check if any number between 2 and the square root of the current number divides the current number without a remainder. If no such number is found, the current number is added to the list of primes.