"""
multithreading: Split one process into multiple pieces and run in parallel.
each piece is called THREAD
Library: threading
- multithreading is not parallel
- then what is the use of multithreading if not parallel?
    -- if one thread is waiting for some resource then
    during that waiting time, it will execute another thread
So, FINALLY, in multithreading we are making use waiting time of the thread


multiprocessing: We can create one program into multiple processes and
run all process in parallel
Library: multiprocess
100% multiprocessing is parallel

"""

print("WITHOUT Using multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print(f"Square of {i}:", i*i)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
my_square_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
############################

print("USING multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print(f"Square of {i}:", i*i)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
L1 = L[:4]
L2 = L[4:]

from threading import Thread
thread_1 = Thread(target=my_square_function, args=(L1,))
thread_2 = Thread(target=my_square_function, args=(L2,))

# start() will start the thread,
# but it will not wait for thread execution to complete
thread_1.start()
thread_2.start()

# We can make thread to wait till it completes
thread_1.join()
thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
############################

print("WITH DELAY: WITHOUT Using multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print(f"Square of {i}:", i*i)
        time.sleep(0.1)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
my_square_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
############################

print("WITH DELAY: USING multithreading")
print("-"*20)
# -------------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print(f"Square of {i}:", i*i)
        time.sleep(0.1)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
L1 = L[:4]
L2 = L[4:]

from threading import Thread
thread_1 = Thread(target=my_square_function, args=(L1,))
thread_2 = Thread(target=my_square_function, args=(L2,))

# start() will start the thread,
# but it will not wait for thread execution to complete
thread_1.start()
thread_2.start()

# We can make thread to wait till it completes
thread_1.join()
thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
############################