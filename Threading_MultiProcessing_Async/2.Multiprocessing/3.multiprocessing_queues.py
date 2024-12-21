from multiprocessing import Process, Queue
import time

# Define a function to perform a computational task
def check_value_in_list(x,i,numbe_of_processes,queue):
    # Iterate over a large range and check if elements are in the list
    max_number_to_check = 10**8
    lower_bound = int(i * max_number_to_check / numbe_of_processes)
    upper_bound = int((i+1) * max_number_to_check / numbe_of_processes)
    number_of_hits = 0
    for i in range(lower_bound,upper_bound):  # Reduced iterations for practical execution
        if i in x : number_of_hits+=1

    queue.put((lower_bound,upper_bound,number_of_hits))

if __name__ == '__main__':
    # Define a list for comparison
    comparison_list = [1, 2, 3]
    queue = Queue()

    # Number of processes to run in parallel
    num_process = 4
    processes = []

    # Measure the start time
    start_time = time.time()

    # Create and start processes
    for i in range(num_process):
        process = Process(target=check_value_in_list, args=(comparison_list,i, num_process,queue))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    queue.put('Done')

    while True:
        v = queue.get()
        if v == 'Done':
            break
        lower,upper,number_of_hits = v
        print('Between',lower,'and',upper,'we have', number_of_hits, 'values in the list')
    # Measure the end time
    end_time = time.time()

    # Print the time taken for execution
    print('Time taken:', (end_time - start_time), 'seconds')
