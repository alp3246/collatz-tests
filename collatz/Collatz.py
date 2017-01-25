#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------
cache = [] 
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
    assert n > 0
    m = n
    assert m > 0
    return m

def create_cache(n) :
    global cache
    for i in range(n) :
        cache.append(cycle_len(i))

def next_num (cur):
    if cur % 2 ==0 :
        return cur / 2
    else :
        return 3 * cur + 1

def cycle_len (cur) :
    count = 1
    while cur > 1 :
        cur = next_num(cur)
        if cur < len(cache) :
            return count + cache[cur]
        if (cur &(cur-1) == 0) : #determines if power of 2
                return count + math.log(cur,2)
        count = count + 1
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

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)
