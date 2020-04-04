t = int(input())
jj=1
while t:
    s=list(input())
    arr=[0]*len(s)
    lst=list(s)
    ans=""
    di={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    for i in range(len(s)):
        arr[i] = di[s[i]]-di['0']
    temp=0
    for i in range(len(s)):
        dd=abs(arr[i]-temp)
        if arr[i]>temp:
            while dd:
                ans = ans + "(" 
                dd= dd-1
        if arr[i]<temp:
            while(dd):
                ans = ans + ")"
                dd = dd-1
        temp = arr[i]
        ans = ans + str(temp)
    while(temp):
        ans=ans + ")"
        temp=temp-1
    print("Case #{}:".format(jj),ans)
    jj+=1
    t-=1