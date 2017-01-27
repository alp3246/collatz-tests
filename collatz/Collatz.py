#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
import sys
import math
# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------

#GLOBALS
global cache 
global maxVal
global maxIndex

cache = []
eager = []
maxVal = 1
maxIndex = 1

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# ------------
# collatz_eval
# ------------

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    return the max cycle length of the range [1, n]
    """
    # <your code>
    #global cache
    #global maxVal
    #global maxIndex
    if n > len(eager) :
        create_cache(1000)
    if n < eager[len(eager) - 1] :
        return search_cache(n)

    assert n > 0
    
    m = 1
    mi = 1
    i = 1
    
    while i <= n :
        cur = cache[i]
        if cur >= m :
            m = cur
            mi = i
        i = i + 1
    assert mi > 1
    maxVal = m
    maxIndex = mi
    return mi

def create_cache(n): #append_list(n):
    #global cache
    cache = []
    eager.append(1)
    cache.append(1)
    curMaxLength = cache[0]
    assert n > len(cache)
    i = 2
    while i < n :
        cur = cycle_len(i)
        cache.append(int(cur))
        if cur >= curMaxLength :
            eager.append(int(i))
            curMaxLength = cur
        i = i + 1
"""
def eager_cache(n):
    #curMaxLength = cache[0]
    eager.append(1)
    i = 1
    while i <= n :
        cur = cache[i]
        if cur > eager[len(eager) - 1] :
            eager.append(int(i))
            i = i + 1      
"""
def search_cache(n) :
    assert n < eager[len(eager)-1]
    i = len(eager)
    while n < eager[i-1] :
        i = i - 1
    return eager[i-1]

def cycle_len (cur) :
    count = 1
    while cur > 1 :
        if cur % 2 == 0 :
            cur = cur // 2
        else :
            cur = ( 3 * cur ) + 1
        count = count + 1
        if cur & (cur-1) == 0 :
            return count + int(math.log(cur,2))
    return count

def rangeMax(a,b):
    cur = 1
    loc = 1
    while a <= b:
        tmp = cycle_len(a)
        if  tmp >= cur :
            cur = tmp
            loc = a
        a = a + 1
    return loc   
# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

def print_debug(w):
    w.write("cycle_len3 test:" +str(cycle_len(3)) + "\n\texpect 8\n")
    w.write("cycle_len4 test:" +str(cycle_len(4)) + "\n\texpect 3\n")
    w.write("cycle_len7 test:" +str(cycle_len(7)) + "\n\texpect 17\n")
    w.write("Cache:\n")
    for i in range(30):
        w.write(str(cache[i]) + " ")
    w.write("\nEager:\n")
    for i in range(10):
        w.write(str(eager[i]) + " ")
    w.write("\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    create_cache(1000)
    #eager_cache(1000)

    #print_debug(w)

    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)

if __name__ == '__main__':
    collatz_solve(sys.stdin, sys.stdout)