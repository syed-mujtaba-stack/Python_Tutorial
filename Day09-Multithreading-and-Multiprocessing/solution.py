# Day 9 Solution: Multithreading & Multiprocessing
import threading
import time
from multiprocessing import Process
import os

def print_numbers():
    for i in range(1, 4):
        print('Thread:', i)
        time.sleep(0.5)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

def show_pid():
    print('Process ID:', os.getpid())

process = Process(target=show_pid)
process.start()
process.join()
