from workers.SquaredSumWorkers import SquaredSumWorker
from workers.SleepyWorkers import SleepyWorker
import time


def main():
    calc_start_time  = time.time()

    current_threads = []
    for i in range(5):
        maximum_value = (i+1) * 1000000
        squaredSumWorker = SquaredSumWorker(maximum_value)
        current_threads.append(squaredSumWorker)
    
    for threads in current_threads:
        threads.join()

    calc_end_time  = time.time()
    print('Total Time for  sum of squares : ',round(calc_end_time-calc_start_time,1))

    calc_start_time  = time.time()
    current_threads = []

    for seconds in range(6):
        sleepyWorker = SleepyWorker(seconds,daemon=True)
        current_threads.append(sleepyWorker)
        
    for threads in current_threads:
        threads.join()

    calc_end_time  = time.time()
    print('Total Time for sleep function: ',round(calc_end_time-calc_start_time,1))

if __name__ == '__main__':
    main()
