#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:56:42 2020

@author: Jake
"""

def abbreviation(a, b):
    new = ''
    index = 0
    if a == b:
        return "YES"
    for i in b:
        if i.upper() not in b.upper():
            return "NO"
    for i in a:
        if i.islower() and i.upper() not in b:
            a = a.replace(str(i), '')
    print('first', a)
    for i in a:
        print(i, 'i')
        if b[index::] == '':
            if i .isupper():
                return "NO"
        for j in b[index::]:
            print(j, 'j')
            if i.isupper():
                if j == i:
                    index = b.find(str(j))+1
                    new += j
                    print('if', j, 'index =', index)
                    break
                else:
                    print('else 1', new)
                    return "NO"
            elif i.islower():
                if i.upper() == j or j == i:
                    index = b.find(str(j))+1
                    new += j
                    print('if2', j, 'index =', index)
                    break
                else:
                    print('else 2', new)
                    return 'NO'
    if new.upper() == b.upper():
        return "YES"
    else:
        return "NO"
                    
z = 'beFgH'
h = 'EFG'               
x = 'daBcd'
y = 'ABC'       
#print(z[5::], len(z))

print(abbreviation(x,y))