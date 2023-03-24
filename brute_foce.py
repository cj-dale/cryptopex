import time
from numbthy_master.numbthy import *

print("Brute force factoring")

with open("primes.csv", "r") as file:
    primes = [int(i) for i in file.read().split(",")] # https://stackoverflow.com/questions/69877469/from-a-file-containing-prime-numbers-to-a-list-of-integers-on-python

def brute_force(n):
    start = time.time()
    i = 0
    while 1 == 1:
        if primes[i] > math.ceil(math.sqrt(n)) or i == 999999:
            print("Brute force failed, continuing...")
            return
        if n % primes[i] == 0:
            print("Found a factor =",primes[i])
            print("It took",round(time.time() - start, 2),"seconds")
            return
        i+=1

brute_force(24232273352113381895280635789)


# https://www.programiz.com/python-programming/examples/elapsed-time#:~:text=Example%201%3A%20Using%20time%20module&text=In%20order%20to%20calculate%20the,which%20gives%20the%20execution%20time.