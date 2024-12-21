from multiprocessing import Pool, cpu_count
from functools import partial
import time

# Define a function to perform a computational task
def square(y,additional_param,x):
    return x**y + additional_param
    

if __name__ == '__main__':
    # Define a list for comparison
    comparison_list = [1, 2, 3]

    num_cpu_to_use = max(1,cpu_count()-1)
    print(num_cpu_to_use)

    # Measure the start time
    start_time = time.time()

    power = 3
    additional_param = 2
    partial_function = partial(square,power,additional_param)

    with Pool(num_cpu_to_use) as multiprocessing_pool:
        result = multiprocessing_pool.map(partial_function,comparison_list)


    # Measure the end time
    end_time = time.time()

    # Print the time taken for execution
    print('Time taken:', (end_time - start_time), 'seconds')
    print(result)
