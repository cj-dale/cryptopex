import time
from numbthy_master.numbthy import *

print("Brute force factoring")
start = time.time()
f = factor(498587077741) # print factor pairs
end = time.time()
print("Found a factor =",f[0][0])
print("It took",end-start,"seconds")

# https://www.programiz.com/python-programming/examples/elapsed-time#:~:text=Example%201%3A%20Using%20time%20module&text=In%20order%20to%20calculate%20the,which%20gives%20the%20execution%20time.
