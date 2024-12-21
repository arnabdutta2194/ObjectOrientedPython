from multiprocessing import Pool, cpu_count
import time

# Define a function to perform a computational task
def square(x,y):
    return x**y
    

if __name__ == '__main__':
    # Define a list for comparison
    comparison_list = [1, 2, 3]
    power_list = [4,5,6]

    num_cpu_to_use = max(1,cpu_count()-1)
    print(num_cpu_to_use)

    # Measure the start time
    start_time = time.time() 

    prepared_list = []
    for i in range(len(comparison_list)):
        prepared_list.append((comparison_list[i],power_list[i]))
    print(prepared_list)

    with Pool(num_cpu_to_use) as multiprocessing_pool:
        result = multiprocessing_pool.starmap(square,prepared_list) #[square(1,4),square(2,5),square(3,6)]


    # Measure the end time 
    end_time = time.time()

    # Print the time taken for execution
    print('Time taken:', (end_time - start_time), 'seconds')
    print(result)
