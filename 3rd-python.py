# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 04:49:17 2020

@author: Akshit Patel
"""
t = int(input())
for j in range(t):
    n = int(input())
    d=dict()
    lst=[]
    for i in range(n):
        s,e = map(int,input().split())
        d[s,e]=i
        lst.append([s,e])
    lst.sort()
    a=0
    b=0
    an= ""
    x =True
    ans=[""]*n
    for i in range(n):
        if(a<=lst[i][0]):
            a = lst[i][1]
            ans[d[lst[i][0],lst[i][1]]] = "C"
            del d[lst[i][0],lst[i][1]]
        elif(b<=lst[i][0]):
            b = lst[i][1]
            ans[d[lst[i][0],lst[i][1]]] = "J"
            del d[lst[i][0],lst[i][1]]
        else:
            x = False
            break
    if x:
        for i in ans:
            an = an + i
        print("Case #{}:".format(j+1),an)
    else:
        print("Case #{}:".format(j+1),"IMPOSSIBLE")