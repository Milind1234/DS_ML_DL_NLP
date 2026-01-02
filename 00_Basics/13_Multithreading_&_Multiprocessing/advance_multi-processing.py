###  Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time 

def square_no(number):
    time.sleep(1)
    return f" Sqaure: {number * number}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

if __name__ == "__main__":
    t = time.time()
    with ProcessPoolExecutor(max_workers=3) as excecutor:
        results = excecutor.map(square_no,numbers)

    for result in results:
        print(result)
    
    finished_time = time.time() - t
    print(finished_time)