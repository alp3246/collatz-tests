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
cache = []
eager = [] 
meta = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]

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
    return search_cache(n)

def create_cache(n): #append_list(n):
    global cache
    global eager
    if len(cache) == 0 :
        eager.append(1)
        cache.append(1)
    curMaxLength = cache[len(cache)-1]
    assert n > len(cache)
    i = len(cache)  + 1
    while i < n :
        cur = cycle_len(i)
        cache.append(int(cur))
        if cur >= curMaxLength :
            eager.append(int(i))
            curMaxLength = cur
        i = i + 1

def search_cache(n) :
    #assert n < meta[len(meta)-1]
    i = 0
    if n > meta[len(meta) -1]:
        return meta[len(meta)-1]
    while meta[i] <= n :
        i = i + 1
    return meta[i -1]

def cycle_len (cur) :
    count = 1
    while cur > 1 :
        if cur % 2 == 0 :
            cur = cur // 2
            if cur < len(cache) :
                return count + cache[cur-1]
        else :
            cur = (( 3 * cur ) + 1) // 2
            count = count + 1
        count = count + 1
        if cur & (cur-1) == 0 :
            return count + int(math.log(cur,2))
    return count
  
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

# -------------
# collatz_solve
# -------------

def print_cache(w) :
    i = 0
    while i < len(eager) :
        w.write (str(eager[i]) + ", ")
        i = i + 1 


def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    #only needed to create meta
    #create_cache(5000000)
    #print_cache(w)

    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)

#if __name__ == '__main__':
#    collatz_solve(sys.stdin, sys.stdout)