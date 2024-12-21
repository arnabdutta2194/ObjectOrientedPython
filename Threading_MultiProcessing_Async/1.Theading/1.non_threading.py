import time

def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time  = time.time()
    for i in range(5):
        calculate_sum_squares((i+1) * 1000000)
    
    calc_end_time  = time.time()
    print('Total Time for  sum of squares : ',round(calc_end_time-calc_start_time,1))


    calc_start_time  = time.time()

    for i in range(6):
        sleep_a_little(i)

    calc_end_time  = time.time()
    print('Total Time for sleep function: ',round(calc_end_time-calc_start_time,1))

if __name__ == '__main__':
    main()
