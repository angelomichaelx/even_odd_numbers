# Michael Angelo P. Biag
#BSCPE 1-4
# P-1( 25 points). Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.
# txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

with open("numbers.txt", "r") as sample_file:
    numbers = [int(line.strip()) for line in sample_file]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
