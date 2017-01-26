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
    global cache
    global maxVal
    global maxIndex
    
    assert n > 0
    #if n > len(cache):
    #    append_list(n)
        
    m = 1
    mi = 1
    i = 1
    
    #if n > maxIndex :
     #   i = maxIndex
      #  mi = maxIndex
       # m = maxVal
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
    global cache
    assert n > len(cache)
    i = len(cache)
    while i <= n :
        cur = cycle_len(i)
        cache.append(cur)
        i = i + 1

def eager_cache(n):
    curMaxLength = 1
    curMaxIndex = 1
    cur = 1
    i = curMaxIndex
    while i <= n :
        while cur <= curMaxLength :
            i = i + 1
            cur = rangeMax(1, i)       
        assert i > curMaxIndex
        #global eager
        eager.append(i)
        curMaxIndex = i
        curMaxLength = cur

def search_cache(n) :
    assert n < eager[len(eager)-1]
    i = 0
    while n < eager[i+1] :
        i = i + 1
    return eager[i]

def cycle_len (cur) :
    global cache
    count = 1
    while cur > 1 :
        if cur % 2 == 0 :
            cur = cur // 2
            if cur < len(cache) :
                return count + cache[cur]
        else :
            cur = ( 3 * cur ) + 1
            #check for 2^n
            if (cur &(cur-1) == 0) : 
                return count + 1 + math.log(cur,2)
        count = count + 1
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
    w.write("cycle_len test:" +str(cycle_len(3)))
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
    create_cache(100)
    eager_cache(500)

    #print_debug(w)

    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)

if __name__ == '__main__':
    collatz_solve(sys.stdin, sys.stdout)
"""
def next_num (cur):
    if cur % 2 ==0 :
        return cur/2
    else :
        return 3 * cur + 1

def compute_length(k):
    m = m + 1
    l = next_num(k)
    if l != 1 :
        compute_length(l)

update N with frame a1.
do I = 1 to N with frame a2 down:
    assign j = i M = 0.
    run computeLength( input j).
   display i m.
end.
"""