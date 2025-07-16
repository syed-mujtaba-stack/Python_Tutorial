# Day 18 Solution: Profiling & Optimization
import cProfile
import timeit

def concat_loop():
    s = ''
    for i in range(1000):
        s += str(i)
    return s

cProfile.run('concat_loop()')

# Compare with join
loop_time = timeit.timeit('"".join([str(i) for i in range(1000)])', number=1000)
concat_time = timeit.timeit('s=""\nfor i in range(1000): s+=str(i)', number=1000)
print('join:', loop_time, 'concat:', concat_time)
