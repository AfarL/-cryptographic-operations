from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
import hashlib
import time
import random
from Cryptodome.Random import get_random_bytes
from tate_bilinear_pairing import eta
from tate_bilinear_pairing import ecc


sum=0
i=1
for i in range(1000):
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    g = ecc.gen()
    inf1, x1, y1 = ecc.scalar_mult(a, g)
    inf2, x2, y2 = ecc.scalar_mult(b, g)
    t1 = time.perf_counter()
    t = eta.pairing(x1, y1, x2, y2)
    t2 = time.perf_counter()
    sum = sum + t2 - t1

print("Total time of 1000 times tate_bilinear_pairing operation:", sum)
print("Average time of tate_bilinear_pairing operation:", sum/1000)


