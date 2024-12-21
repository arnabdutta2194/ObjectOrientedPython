from multiprocessing import Pool, cpu_count, Manager
import time

# Define a function to perform a computational task
def check_value_in_list(comp_list, lower, upper, queue):
    """
    Check how many numbers in the range [lower, upper) are present in comp_list.

    Args:
        comp_list (list): List of values to compare.
        lower (int): Lower bound of the range (inclusive).
        upper (int): Upper bound of the range (exclusive).
        queue (Queue): A multiprocessing queue to store results.

    Returns:
        None
    """
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            number_of_hits += 1
    queue.put((lower, upper, number_of_hits))

if __name__ == '__main__':
    # Define a list for comparison
    comparison_list = [1, 2, 3]

    # Define the range splits for the task
    lower_and_upper_bounds = [
        (0, 25 * 10**6),
        (25 * 10**6, 50 * 10**6),
        (50 * 10**6, 75 * 10**6),
        (75 * 10**6, 100 * 10**6)
    ]

    # Create a manager to share the queue among processes
    manager = Manager()
    queue = manager.Queue()

    # Determine the number of CPU cores to use
    num_cpu_to_use = max(1, cpu_count() - 1)
    print(f"Using {num_cpu_to_use} CPUs")

    # Measure the start time
    start_time = time.time()

    # Prepare the arguments for starmap
    prepared_list = [
        (comparison_list, lower, upper, queue)
        for lower, upper in lower_and_upper_bounds
    ]

    # Use a multiprocessing pool to process the tasks
    with Pool(num_cpu_to_use) as multiprocessing_pool:
        multiprocessing_pool.starmap(check_value_in_list, prepared_list)

    # Retrieve results from the queue
    results = []
    while not queue.empty():
        results.append(queue.get())

    # Measure the end time
    end_time = time.time()

    # Print the time taken for execution
    print('Time taken:', (end_time - start_time), 'seconds')

    # Print the results
    print("Results:")
    for result in sorted(results):
        print(f"Range {result[0]} to {result[1]}: {result[2]} hits")
