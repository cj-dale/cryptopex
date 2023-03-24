import time
import random
import math
from numbthy_master.numbthy import *

start_dixon = time.time()

with open("primes.csv", "r") as file:
    primes = [int(i) for i in file.read().split(",")] # https://stackoverflow.com/questions/69877469/from-a-file-containing-prime-numbers-to-a-list-of-integers-on-python

n = 124076833

def prime_factorization(n, factor_base):
    factors = [0] * len(factor_base)
    for i, j in enumerate(factor_base): # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        if time.time() - start_dixon >= 240:
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
print("Done generating factor base.")

# https://www.geeksforgeeks.org/construct-unique-matrix-n-x-n-input-n/

good_equation_matrix = [[0 for j in range(len(factor_base))] for i in range(len(factor_base) + 1)] # add more in range "for i" to add more rows

def generate_matrix(factor_base):
    if time.time() - start_dixon >= 240:
            exit()
    for i in range(len(good_equation_matrix)):
        if time.time() - start_dixon >= 240:
            exit()
        good_equation = False
        while good_equation == False:
            x = random.randint(4, n - 2) % n
            good_equation = prime_factorization(x ** 2, factor_base)
            good_equation_matrix[i] = x, good_equation
    return good_equation_matrix

solution_found = False
while 1 == 1:
    print("i'm here")
    if time.time() - start_dixon >= 240:
        exit()
    if solution_found == True:
        break
    good_equation_matrix = generate_matrix(factor_base) # https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
    for i in range(len(good_equation_matrix)):
        print("i'm here now")
        if time.time() - start_dixon >= 240:
            exit()
        if solution_found == True:
            break
        for j in range(len(good_equation_matrix)):
            print("i'm here now, though")
            if i == j:
                continue
            if time.time() - start_dixon >= 240:
                exit()
            if solution_found == True:
                break
            combo = [x + y for x, y in zip(good_equation_matrix[i][1], good_equation_matrix[j][1])]
            for k in combo:
                print("i'm here right now")
                if time.time() - start_dixon >= 240:
                    exit()
                if solution_found == True:
                    break
                if k % 2 != 0:
                    continue
                y = 1
                y *= k
                math.sqrt(y)
                for i in range(len(good_equation_matrix)):
                    print("i'm now here")
                    if time.time() - start_dixon >= 240:
                        exit()  
                    x = good_equation_matrix[i][0]
                    non_trivial = gcd(abs(x - y), n)
                    if non_trivial != 1 and non_trivial != n:
                        solution_found = True
                        break

for i in range(len(good_equation_matrix)):
    print(i + 1, good_equation_matrix[i][0],"===", end=' ')
    print(good_equation_matrix[i][0] ** 2 % n, end = ' ')
    print(good_equation_matrix[i][1])

end_dixon = time.time()
print("\nFound a factor:",non_trivial)
print("It took",round(end_dixon - start_dixon, 2),"seconds")

                        


            
    