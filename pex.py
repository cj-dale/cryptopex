#   pex.py
#  =============================================================
#
#  Name: Caleb Dale
#  Section: Sample M1
#  Project: PEX 1 : I Can Factor That Number In x Seconds
#  Documentation Statement: Used code snippets from various websites (Wikipedia, Stack Overflow, and Progamiz). Links are commented where I used that website specifically.
#  https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm: Used pseudocode to code Pollard's Rho
#  https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops: Learned how to use enumerate() to get both the index and value in one for loop.
#  https://www.programiz.com/python-programming/global-keyword#:~:text=In%20Python%2C%20the%20global%20keyword,variable%20in%20a%20local%20context: Used this site to learn how to set a global variable and increment that global variable in a function.
#  https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list: Used this site to learn how to add the values of two lists into new list of the same size.
#  Used PEX1 documentation to ensure guidelines were followed and the Dixon's Algorithm PDF to code dixons().
#  Downloaded code from Numbthy's GitHub repository (https://github.com/Robert-Campbell-256/Number-Theory-Python/blob/master/numbthy.py) and used it for my two calls of gcd().
#  No other help received.
#
#  Comments / Optimizations: I ran the calculations on my cadet issued laptop (Intel i7-8665U). If I had run them on my personal computer (AMD Ryzen 7 5800x), the calculations
#  would have been faster.
#  Some opportunity for optimization I had was with Dixon's Algorithm. My code generates a full matrix of good equations the length and height of the factor base before checking all of them against each other.
#  If I did it smarter, I would have generated two good equations, compared them, generated one more, compared those three, and so on. I also could have checked for combinations of more than 2. I only check for two good equations combined.
#  I performed tests for the test cases that Dixon's wasn't able to solve. I tested for the highest ratio of equations solved to equations needed to estimate an optimal factor base.
#  Based on my tests, if I implemented the optimizations above, I would guess that the optimal factor base for test case f (24232273352113381895280635789) would be around 230.
#  Similarly, I would also givee that the best factor base for test case g (213016805697990920376675714115937442919) would be around 380.
#  
#  Slightly modified my code to more elequantly print what attempt I was on for Pollard's Rho inbetween my screenshots for test case f and g.
# =============================================================

import time
import math
from numbthy_master.numbthy import *

print("PEX1 - Factoring! - by Cadet Dale\nCyS431")

with open("primes.csv", "r") as file:
    primes = [int(i) for i in file.read().split(",")]

a = 2 # setting a, b, and d for pollard's rho
b = 2
d = 1

def pollards_rho(n, start_time, attempt): # pseudocode from https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    print("Pollard's Rho - attempt #",attempt)
    
    global a, b, d # making them global so that if it fails it doesn't just do the same numbers

    while d == 1: # while d is non-trivial
        a = (a**2 + 1) % n
        b = (((b**2 + 1)**2) + 1) % n
        d = gcd(abs(a - b), n)
        if time.time() - start_time >= 120: # over 2 minutes check
            print("Attempt took over 2 minutes.\n")
            return False
    if d == n: # d is the number, pollard's rho failed
        print("Did not find a factor")
        return False
    else:
        print("Found a factor =",d)
    print("a =", a,"b =", b)
    print("It took", round(time.time() - start_time, 2),"seconds.\n")
    return True

def prime_factorization(n, factor_base, start_time):
    factors = [0] * len(factor_base) # generate list of zeroes the length of factor base
    for i, j in enumerate(factor_base): # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        if time.time() - start_time >= 120: # time check
            return False
        while n % j == 0: # n is divisible by that number that is in the factor base
            n /= j # divide it out
            factors[i] += 1 # add one to that list of factors that make up the number
        if n == 1: # factors[] finished!
            break
    if n != 1 and n not in factor_base: # number not able to be formed with that factor base
        return False
    return factors

def brute_force(n, primes, start_time):
    print("\nBrute force factoring")
    i = 0
    while 1 == 1:
        if primes[i] > math.ceil(math.sqrt(n)) or i == 999999: # checks if the square root of n is greater than a number in factor base
            print("Brute force failed. Square root of n is larger than millionth prime. Continuing...\n")
            return
        if n % primes[i] == 0: # checks for divisability at that index in primes[]
            print("Found a factor =",primes[i])
            print("It took", round(time.time() - start_time, 2),"seconds.\n")
            return
        i+=1

def get_input():
    n = 1
    n = input("\nEnter a number to factor: ")
    if int(n) <= 0: # checks for zero or negative input
        print("Non-positive integer entered. Exiting.")
        exit(-1)
    else:
        return(int(n))

def generate_matrix(good_equation_matrix, factor_base, start_time): # generate good equations until a matrix the length and height of the factor base is complete with good ones
    global k # https://www.programiz.com/python-programming/global-keyword#:~:text=In%20Python%2C%20the%20global%20keyword,variable%20in%20a%20local%20context.
    for i in range(len(good_equation_matrix)):
        good_equation = False
        while good_equation == False:
            if time.time() - start_time >= 120: # return empty matrix if it takes too long
                return [[0 for j in range(len(factor_base))] for i in range(len(factor_base) + 1)]
            x = math.ceil(math.sqrt((k) * n))
            k+=1
            good_equation = prime_factorization((x ** 2) % n, factor_base, start_time)
            good_equation_matrix[i] = x, good_equation
    return good_equation_matrix

def dixons(n, primes, start_time):

    print("Dixon's Algorithm")
    num_factors = input("Enter # of factors in factor base: ")
    factor_base = primes[:int(num_factors)]
    print("Done generating factor base.")

    while 1 == 1: # keeps going until time is up or a solution is found
        if time.time() - start_time >= 120:
            return False
        good_equation_matrix = [[0 for j in range(len(factor_base))] for i in range(len(factor_base) + 1)] # add more in range "for i" to add more rows
        good_equation_matrix = generate_matrix(good_equation_matrix, factor_base, start_time)
        if good_equation_matrix == [[0 for j in range(len(factor_base))] for i in range(len(factor_base) + 1)]:
            return False
        for i in range(len(good_equation_matrix)):
            if time.time() - start_time >= 120:
                return False
            for j in range(len(good_equation_matrix)):
                if i == j:
                    continue
                if time.time() - start_time >= 120:
                    return False
                combo = [x + y for x, y in zip(good_equation_matrix[i][1], good_equation_matrix[j][1])] # https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
                y = 1
                for i, m in enumerate(combo):
                    if time.time() - start_time >= 120:
                        return False
                    if m % 2 == 0 and m != 0: # if each value in good equation is even
                        y *= (factor_base[i] ** m) # start making y
                for i in range(len(good_equation_matrix)):
                    if time.time() - start_time >= 120:
                        return False
                    x = good_equation_matrix[i][0]
                    non_trivial = gcd(abs(x - round(math.sqrt(y))), n) # check for non trivial factor
                    if non_trivial != 1 and non_trivial != n: # non trivial factor found! start outputting success
                        for i in range(len(good_equation_matrix)): # print successful equations
                            print("",i + 1, good_equation_matrix[i][0],"===", end=' ')
                            print(good_equation_matrix[i][0] ** 2 % n, end = ' ')
                            for j in range(len(good_equation_matrix[i][1])):
                                print(good_equation_matrix[i][1][j], end = " ")
                            print()
                        print("Found a factor:",non_trivial)
                        print("It took",round(time.time() - start_time, 2),"seconds.")
                        return True

n = 1
while 1 == 1:

    start_time = time.time()

    n = get_input()

    brute_force(n, primes, time.time())

    for i in range(3): # try 3 times
        if pollards_rho(n, time.time(), i + 1) == True:
            break

    k = 1 # initializing global variable k, keeps track of ceil(sqrt(kn)) incrementation

    for i in range(3): # try 3 times
        if dixons(n, primes, time.time()) == True:
            break
        else:
            print("Dixon's took too long or factor base failed.")
            if i < 2:
                print("Trying again.\n")
