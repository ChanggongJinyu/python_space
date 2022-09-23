import cProfile
import palingrams

cProfile.run('palingrams.find_palingrams()')

'''
         62622 function calls in 104.140 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  104.140  104.140 <string>:1(<module>)
        1  104.117  104.117  104.140  104.140 palingrams.py:7(find_palingrams)
        1    0.000    0.000  104.140  104.140 {built-in method builtins.exec}
    60388    0.022    0.000    0.022    0.000 {built-in method builtins.len}
     2230    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

