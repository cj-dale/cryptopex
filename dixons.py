import time
import csv

with open("primes.csv", "r") as file:
    primes = [int(i) for i in file.read().split(",")] # https://stackoverflow.com/questions/69877469/from-a-file-containing-prime-numbers-to-a-list-of-integers-on-python

n = 802432
