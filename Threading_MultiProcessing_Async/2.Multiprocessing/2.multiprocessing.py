from multiprocessing import Process
import time

# Define a function to perform a computational task
def check_value_in_list(x,):
    # Iterate over a large range and check if elements are in the list
    for i in range(10**8):  # Reduced iterations for practical execution
        if i in x : print("Found")


if __name__ == '__main__':
    # Define a list for comparison
    comparison_list = [1, 2, 3]

    # Number of processes to run in parallel
    num_process = 4
    processes = []

    # Measure the start time
    start_time = time.time()

    # Create and start processes
    for i in range(num_process):
        process = Process(target=check_value_in_list, args=(comparison_list,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Measure the end time
    end_time = time.time()

    # Print the time taken for execution
    print('Time taken:', (end_time - start_time), 'seconds')
