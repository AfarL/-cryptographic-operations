import time
from pypuf.simulation import XORArbiterPUF
from pypuf.io import random_inputs

puf = XORArbiterPUF(n=64, k=2, seed=1)
challenges = random_inputs(n=64, N=1, seed=2)
sum=0
i=1
for i in range(1000):
    t1 = time.perf_counter()
    puf.eval(challenges)
    t2 = time.perf_counter()
    sum=sum+t2-t1
print("Total time of 1000 times XORArbiterPUF operation:", sum)
print("Average time of XORArbiterPUF operation:", sum/1000)
