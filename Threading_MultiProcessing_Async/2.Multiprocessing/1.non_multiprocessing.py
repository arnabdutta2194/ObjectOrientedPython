from threading import Thread
import time

def check_value_in_list(x):
    for i in range(10**8):
        if i in x : print("Found")

comparison_list = [1,2,3]
num_thread = 4
threads = []

start_time = time.time()
for i in range(num_thread):
    t = Thread(target=check_value_in_list,args=(comparison_list,))
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print('Time taken',(end_time-start_time),'second')