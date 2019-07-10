import primes_cython, primes_cythonize, primes_python
import time
import numpy as np

def primes_time(func):
    times = []
    for i in range(100):
        start = time.time()
        func.primes(1000)
        end = time.time()
        total_time = end-start
        total_time = round(total_time * 1000, 2)
        times.append(total_time)
    print('Function:', func.__name__) 
    print('Mean:', round(np.mean(times), 2), 'ms')
    print('STD', round(np.std(times), 2), 'ms')
    print()
    
if __name__ == '__main__':
    primes_time(primes_cython)
    primes_time(primes_cythonize)
    primes_time(primes_python)