
import time
import matplotlib.pyplot as plt

def original_func(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)


def improved_func(n, memory={}):
    if n in memory:
        return memory[n]
    elif n == 0 or n == 1:
        return n
    memory[n] = improved_func(n-1, memory) + improved_func(n-2, memory)
    return memory[n]


integers = range(36)
original_times = []
improved_times = []

for n in integers:
    start = time.time()
    original_func(n)
    original_times.append(time.time() - start)
    
    start = time.time()
    improved_func(n)
    improved_times.append(time.time() - start)


plt.plot(integers, original_times, label='Original time')
plt.plot(integers, improved_times, label='Improved time')
plt.xlabel('Integers (0 to 35)')
plt.ylabel('Time (s)')
plt.legend()
plt.show()