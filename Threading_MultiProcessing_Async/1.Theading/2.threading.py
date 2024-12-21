import time
import threading


def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2
    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time  = time.time()

    current_threads = []
    for i in range(5):
        maximum_value = (i+1) * 1000000
        t = threading.Thread(target=calculate_sum_squares,args=(maximum_value,))
        # t = threading.Thread(target=calculate_sum_squares,args=(maximum_value,),daemon=True) #--- Daemon=True signifies that all the threads do not need to finish untill the program finishes
        t.start()
        current_threads.append(t)
    for threads in current_threads:
        threads.join()
    
    calc_end_time  = time.time()
    print('Total Time for  sum of squares : ',round(calc_end_time-calc_start_time,1))


    calc_start_time  = time.time()
    current_threads = []

    for seconds in range(6):
        t = threading.Thread(target=sleep_a_little,args=(seconds,))
        t.start()
        # t.join() #--- This means execution is blocked till the end of execution of this thread
        current_threads.append(t)
    for threads in current_threads:
        threads.join()


    calc_end_time  = time.time()
    print('Total Time for sleep function: ',round(calc_end_time-calc_start_time,1))

if __name__ == '__main__':
    main()
