# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:30:13 2020

@author: Joseph
"""

def lineint(a1,a2,b1,b2):
    alist = [a1,a2]
    blist = [b1,b2]
    
    #sort in case the two points were entered out of order
    alist.sort()
    blist.sort()
    
    #check to make sure lines intersect
    if (alist[0] > blist[1]) or (blist[0] > alist[1]):
        return 0
    
    else:
        biglist = alist + blist
        biglist.sort()
        intersection = biglist[2] - biglist[1]
        return intersection


