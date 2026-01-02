### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_no():
    for i in range(5):
        time.sleep(2)
        print(i)

def print_alpha():
    for letter in 'abcde':
        time.sleep(2)
        print(letter)

t = time.time()
print_no()
print_alpha()
finished_time = time.time() - t
print(finished_time)

print("_______( Muli-Threading )")

t1 = threading.Thread(target = print_no)
t2 = threading.Thread(target = print_alpha)

time1 = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
finished_time1 = time.time() -time1
print(finished_time1)
