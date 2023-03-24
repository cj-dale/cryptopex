import time
import random
import math
from numbthy_master.numbthy import *

start_time = time.time()

with open("primes.csv", "r") as file:
    primes = [int(i) for i in file.read().split(",")]

def get_input():
    n = input("Enter a number to factor: ")
    return int(n)

n = get_input()

def brute_force(n, primes, start_time):
    start = time.time()
    i = 0
    while 1 == 1:
        if primes[i] > math.ceil(math.sqrt(n)) or i == 999999:
            print("Brute force failed, continuing...")
            return
        if n % primes[i] == 0:
            print("Found a factor =",primes[i])
            print("It took", round(time.time() - start_time, 2),"seconds\n")
            return
        i+=1

brute_force(n, primes, time.time())

print("Pollard's Rho")
start_time = time.time()

def pollards_rho(n, primes, start_time): # pseudocode from https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    a = 2
    b = 2
    d = 1

    while d == 1:
        a = (a**2 + 1) % n
        b = (((b**2 + 1)**2) + 1) % n
        d = gcd(abs(a - b), n)
        if time.time() - start_time >= 240:
            print("Pollard's Rho took over 2 minutes. Trying again...")

    if d == n:
        print("Did not find a factor")
        return False
    else:
        print("Found a factor =",d)
    print("a =", a,"b =", b)
    print("It took", round(time.time() - start_time, 2),"seconds\n")
    return True

solution_found = False
for i in range(3):
    if pollards_rho(n, primes, time.time()) == True:
        solution_found = True
        break

def prime_factorization(n, factor_base):
    factors = [0] * len(factor_base)
    for i, j in enumerate(factor_base): # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        if time.time() - start_time >= 240:
            exit()
        while n % j == 0:
            n /= j
            factors[i] += 1
        if n == 1:
            break
    if n != 1 and n not in factor_base:
        return False
    return factors

num_factors = input("Enter # of factors in factor base: ")

factor_base = primes[:int(num_factors)]
good_equation_matrix = [[0 for j in range(len(factor_base))] for i in range(len(factor_base) + 1)] # add more in range "for i" to add more rows

def generate_matrix(factor_base):
    if time.time() - start_time >= 240:
            print("Matrix generation took too long. Continuing...")
            return
    for i in range(len(good_equation_matrix)):
        if time.time() - start_time >= 240:
            print("Matrix generation took too long. Continuing...")
            return
        good_equation = False
        while good_equation == False:
            x = random.randint(4, n - 2) % n
            good_equation = prime_factorization(x ** 2, factor_base)
            good_equation_matrix[i] = x, good_equation
    return good_equation_matrix

def dixons(n, primes, start_time):
    print("\nDone generating factor base.")

    solution_found = False
    while 1 == 1:
        if time.time() - start_time >= 240:
            exit()
        if solution_found == True:
            break
        good_equation_matrix = generate_matrix(factor_base) # https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
        for i in range(len(good_equation_matrix)):
            if time.time() - start_time >= 240:
                exit()
            if solution_found == True:
                break
            for j in range(len(good_equation_matrix)):
                if i == j:
                    continue
                if time.time() - start_time >= 240:
                    exit()
                if solution_found == True:
                    break
                combo = [x + y for x, y in zip(good_equation_matrix[i][1], good_equation_matrix[j][1])]
                for k in combo:
                    if time.time() - start_time >= 240:
                        exit()
                    if solution_found == True:
                        break
                    if k % 2 != 0:
                        continue
                    y = 1
                    y *= k
                    math.sqrt(y)
                    for i in range(len(good_equation_matrix)):
                        if time.time() - start_time >= 240:
                            exit()  
                        x = good_equation_matrix[i][0]
                        non_trivial = gcd(abs(x - y), n)
                        if non_trivial != 1 and non_trivial != n:
                            solution_found = True
                            break

    if solution_found == False:
        print("Factor base combinations took too long. Continuing...")
        return False

    for i in range(len(good_equation_matrix)):
        print(i + 1, good_equation_matrix[i][0],"===", end=' ')
        print(good_equation_matrix[i][0] ** 2 % n, end = ' ')
        print(good_equation_matrix[i][1])

    print("\nFound a factor:",non_trivial)
    print("It took",round(time.time() - start_time, 2),"seconds")
    return True

solution_found = False
for i in range(2):
    if dixons(n, primes, time.time()) == True:
        solution_found = True
        exit()

if dixons(n, primes, time.time()) == False:
    print("Dixon's took too long or factor base failed.")
