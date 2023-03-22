import time
from numbthy_master.numbthy import *

print("Pollard's Rho")
start = time.time()

n = 498587077741
a = 2
b = 2
d = 1

while d == 1:
    a = (a**2 + 1) % n
    b = (((b**2 + 1)**2) + 1) % n
    d = gcd(abs(a - b), n)

end = time.time()

if d == n:
    print("Did not find a factor")
else:
    print("Found a factor =",d)
print("a =", a,"b =", b)
print("It took",end-start,"seconds")

# pseudocode from https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm