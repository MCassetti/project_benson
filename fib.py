#! /usr/env python 
# linear time fibbonacci
def fib(x):
    a,b = 0,1

    for counter in range(x+1):
        a,b = b, a+b
    return b


