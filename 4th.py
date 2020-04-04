l1=[int(i) for i in input().split()]
while l1[0]:
    l2=[]
    for i in range(l1[1]):
        print(i+1)
        l22=input()
        l2.append(l22)
    for i in range(l1[1]):
        print(l2[i],end="")
    print()
    c=input()
    if c=='N':
        break
    l1[0]-=1