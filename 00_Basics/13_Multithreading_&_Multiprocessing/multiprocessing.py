# Proceesses that runs in parallel
# CPU-bound Tasks - Tasks that are heavy on CPU usage(e.g., mathematical computations,data processing).
# Parallel execution - Multiple core of the CPU

import multiprocessing
import time 

def square_no():
    for i in range(5):
        time.sleep(1)
        print(i**2)

def cube_no():
    for i in range(5):
        time.sleep(5)
        print(i**3)
    

if __name__ == "__main__":
    # Create 2 processes 
    p1 = multiprocessing.Process(target=square_no)
    p2 = multiprocessing.Process(target=cube_no)
    t = time.time()

    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)