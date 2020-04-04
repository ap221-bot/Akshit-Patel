t=int(input())
jj=1
while(t):
    n=int(input())
    sum=0
    r=0
    c=0
    l2=[]
    l3=[]
    l9=[]
    for uu in range(n):
        l1=[int(i) for i in input().split()]
        l2.append(l1)
        l3=l3+l1
    i=0
    for u in range(n):
        sum=sum+l2[i][i]
        i+=1
    ii=0
    for l in range(n):
        l4=set(l2[l])
        if len(l4)!=n:
            r=r+1
        else:
            continue
    
    for d in range(n):
        s=set()
        for dd in range(n):
            s.add(l2[dd][d])
        if len(s)!=n:
            c=c+1

    print("Case #{}:".format(jj),sum,r,c)
    jj+=1
    t-=1