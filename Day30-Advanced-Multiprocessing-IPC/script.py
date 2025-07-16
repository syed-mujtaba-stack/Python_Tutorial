# Day 30 Script: Advanced Multiprocessing & IPC Demo
from multiprocessing import shared_memory
import numpy as np

# Create shared memory array
arr = np.array([1, 2, 3, 4])
shm = shared_memory.SharedMemory(create=True, size=arr.nbytes)
shm_arr = np.ndarray(arr.shape, dtype=arr.dtype, buffer=shm.buf)
shm_arr[:] = arr[:]
print('Shared memory array:', shm_arr)
shm.close()
shm.unlink()
