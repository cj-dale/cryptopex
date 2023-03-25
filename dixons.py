#   pex.py
#  =============================================================
#  Name: Caleb Dale
#  Section: Sample M1
#  Project: PEX 1 : I Can Factor That Number In x Seconds
#  Documentation Statement: Used F21 CS210 C reference guide. No other
#  help received.
# =============================================================

import time
import math
from numbthy_master.numbthy import *

print("PEX1 - Factoring! - by Cadet Dale\nCyS431")

with open("primes.csv", "r") as file:
    primes = [int(i) for i in file.read().split(",")]

def prime_factorization(n, factor_base, start_time):
    factors = [0] * len(factor_base)
    for i, j in enumerate(factor_base): # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        if time.time() - start_time >= 120:
            return False
        while n % j == 0:
            n /= j
            factors[i] += 1
        if n == 1:
            break
    if n != 1 and n not in factor_base:
        return False
    return factors

def get_input():
    n = 1
    n = input("\nEnter a number to factor: ")
    if int(n) <= 0:
        print("Non-positive integer entered. Exiting...")
        exit()
    else:
        return(int(n))

def generate_matrix(good_equation_matrix,factor_base, start_time):
    global k
    for i in range(len(good_equation_matrix)):
        good_equation = False
        while good_equation == False:
            x = math.ceil(math.sqrt((k) * n))
            k+=1
            good_equation = prime_factorization((x ** 2) % n, factor_base, start_time)
            good_equation_matrix[i] = x, good_equation
            if time.time() - start_time >= 10:
                print("It took 10 seconds to generate",i,"good equations. The ratio of good equations I have to ones I need is",i/len(factor_base))
                exit()
    return good_equation_matrix

def dixons(n, num_factors, primes, start_time):
    print("Dixon's Algorithm")
    factor_base = primes[:int(num_factors)]
    print("Done generating factor base.")

    while 1 == 1:
        if time.time() - start_time >= 120:
            return False
        good_equation_matrix = [[0 for j in range(len(factor_base))] for i in range(len(factor_base))] # add more in range "for i" to add more rows
        good_equation_matrix = generate_matrix(good_equation_matrix, factor_base, start_time) # https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
        for i in range(len(good_equation_matrix)):
            if time.time() - start_time >= 120:
                return False
            for j in range(len(good_equation_matrix)):
                if i == j:
                    continue
                if time.time() - start_time >= 120:
                    return False
                combo = [x + y for x, y in zip(good_equation_matrix[i][1], good_equation_matrix[j][1])]
                y = 1
                for i, m in enumerate(combo):
                    if time.time() - start_time >= 120:
                        return False
                    if m % 2 == 0 and m != 0:
                        y *= (factor_base[i] ** m)
                for i in range(len(good_equation_matrix)):
                    if time.time() - start_time >= 120:
                        return False
                    x = good_equation_matrix[i][0]
                    non_trivial = gcd(abs(x - round(math.sqrt(y))), n)
                    if non_trivial != 1 and non_trivial != n:
                        for i in range(len(good_equation_matrix)):
                            print("",i + 1, good_equation_matrix[i][0],"===", end=' ')
                            print(good_equation_matrix[i][0] ** 2 % n, end = ' ')
                            for j in range(len(good_equation_matrix[i][1])):
                                print(good_equation_matrix[i][1][j], end = " ")
                            print()
                        print("Found a factor:",non_trivial,"using factor base size",i)
                        print("It took",round(time.time() - start_time, 2),"seconds.")
                        return True

n = 1
while 1 == 1:

    start_time = time.time()

    n = get_input()

    k = 1
    i = 385

    print("Factoring",n,"with factor base",i)
    if dixons(n, i, primes, time.time()) == True:
        start_time = time.time()
        exit()
    else:
        continue
        
