from multiprocessing import Pool, cpu_count
import time

# Define a function to perform a computational task
def square(x):
    return x**2
    

if __name__ == '__main__':
    # Define a list for comparison
    comparison_list = [1, 2, 3]

    num_cpu_to_use = max(1,cpu_count()-1)
    print(num_cpu_to_use)

    # Measure the start time
    start_time = time.time()

    with Pool(num_cpu_to_use) as multiprocessing_pool:
        result = multiprocessing_pool.map(square,comparison_list)


    # Measure the end time
    end_time = time.time()

    # Print the time taken for execution
    print('Time taken:', (end_time - start_time), 'seconds')
    print(result)
