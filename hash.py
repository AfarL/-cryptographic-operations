import time
import hashlib

sum=0
i=1
for i in range(1000):

    string = "beyongjie"
    t1 = time.perf_counter()
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))  # 注意转码
    res = md5.hexdigest()
    t2 = time.perf_counter()
    sum=sum+t2-t1

print("md5 output:", res)
print("Total time of 1000 times md5 operation:", sum)
print("Average time of md5 operation:", sum/1000)
