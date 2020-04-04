t = int(input())
jj=1
while t:
    l=[int(i) for i in input().split()]
    n=l[0]
    k=l[1]
    if n==2:
        if k==2:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2")
            print("2 1")
        elif k==4:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("2 1")
            print("1 2")
        else:
            print("Case #{}:".format(jj),"IMPOSSIBLE")
    elif n==3:
        if k==3:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 3")
            print("3 1 2")
            print("2 3 1")
        elif k==6:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("2 1 3")
            print("3 2 1")
            print("1 3 2")
        elif k==9:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("3 2 1")
            print("1 3 2")
            print("2 1 3")
        else:
            print("Case #{}:".format(jj),"IMPOSSIBLE")
    elif n==4:
        if k==4:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 3 4")
            print("2 1 4 3")
            print("3 4 1 2")
            print("4 3 2 1")
        elif k==6:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 3 4")
            print("2 1 4 3")
            print("3 4 2 1")
            print("4 3 1 2")
        elif k==7:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 1 3 2")
            print("1 4 2 3")
            print("3 2 1 4")
            print("2 3 1 1")
        elif k==8:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("2 1 3 4")
            print("1 2 4 3")
            print("3 4 2 1")
            print("4 3 1 2")
        elif k==9:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 3 4 2")
            print("3 2 1 4")
            print("2 4 3 1")
            print("4 1 2 3")
        elif k==10:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 1 3 2")
            print("1 4 2 3")
            print("3 2 1 4")
            print("2 3 4 1")
        elif k==11:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 2 1 3")
            print("1 4 3 2")
            print("3 1 2 4")
            print("2 3 4 1")
        elif k==12:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 2 1 3")
            print("2 4 3 1")
            print("1 3 2 4")
            print("3 1 4 2")
        elif k==13:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 3 2 1")
            print("2 4 1 3")
            print("1 2 3 4")
            print("3 1 4 2")
        elif k==14:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 3 2 1")
            print("3 4 1 2")
            print("1 2 3 4")
            print("2 1 4 3")
        elif k==16:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("4 1 2 3")
            print("1 4 3 2")
            print("3 2 4 1")
            print("2 3 1 4")
        else:
            print("Case #{}:".format(jj),"IMPOSSIBLE")    
    elif n==5:
        if k==5:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 3 4 5")
            print("5 1 2 3 4")
            print("4 5 1 2 3")
            print("3 4 5 1 2")
            print("2 3 4 5 1")
        elif k==7:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 4 3 2 5")
            print("2 1 4 5 3")
            print("5 3 2 4 1")
            print("3 2 5 1 4")
            print("4 5 1 3 2")
        elif k==8:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 5 3 2 4")
            print("5 3 2 4 1")
            print("4 2 1 3 5")
            print("2 4 5 1 3")
            print("3 1 4 5 2")
        elif k==20:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 2 1 3 4")
            print("4 5 2 1 3")
            print("3 1 4 2 5")
            print("2 3 5 4 1")
            print("1 4 3 5 2")
        elif k==15:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 3 4 5")
            print("2 3 4 5 1")
            print("3 4 5 1 2")
            print("4 5 1 2 3")
            print("5 1 2 3 4")
        elif k==14:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 1 2 4 3")
            print("3 4 1 5 2")
            print("1 5 3 2 4")
            print("2 3 4 1 5")
            print("4 2 5 3 1")
        elif k==16:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 4 3 5")
            print("2 4 1 5 3")
            print("4 5 3 2 1")
            print("3 1 5 4 2")
            print("5 3 2 1 4")
        elif k==9:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 3 5 4 2")
            print("2 1 3 5 4")
            print("4 5 2 3 1")
            print("3 4 1 2 5")
            print("5 2 4 1 3")
        elif k==10:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("2 1 3 4 5")
            print("5 2 1 3 4")
            print("4 5 2 1 3")
            print("3 4 5 2 1")
            print("1 3 4 5 2")
        elif k==25:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 1 3 4 2")
            print("2 5 1 3 4")
            print("4 2 5 1 3")
            print("3 4 2 5 1")
            print("1 3 4 2 5")
        elif k==11:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 4 3 5 2")
            print("5 1 4 2 3")
            print("3 5 2 4 1")
            print("4 2 1 3 5")
            print("2 3 5 1 4")
        elif k==19:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 4 3 1 2")
            print("1 5 4 2 3")
            print("3 1 2 4 5")
            print("4 2 5 3 1")
            print("2 3 1 5 4")
        elif k==17:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 3 1 4 2")
            print("2 5 3 1 4")
            print("4 1 2 3 5")
            print("3 4 5 2 1")
            print("1 2 4 5 3")
        elif k==21:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 3 1 2 4")
            print("4 5 3 1 2")
            print("2 1 4 3 5")
            print("3 2 5 4 1")
            print("1 4 2 5 3")
        elif k==12:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 4 3 2 5")
            print("4 3 1 5 2")
            print("3 5 2 4 1")
            print("2 1 5 3 4")
            print("5 2 4 1 3")
        elif k==18:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 2 4 5 3")
            print("2 4 1 3 5")
            print("4 3 5 2 1")
            print("5 1 3 4 2")
            print("3 5 2 1 4")
        elif k==13:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("1 3 5 2 4")
            print("4 1 3 5 2")
            print("2 5 4 3 1")
            print("3 2 1 4 5")
            print("5 4 2 1 3")
        elif k==22:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 4 3 2 1")
            print("4 5 1 3 2")
            print("2 1 4 5 3")
            print("1 3 2 4 5")
            print("3 2 5 1 4")
        elif k==23:
            print("Case #{}:".format(jj),"POSSIBLE")
            print("5 1 2 3 4")
            print("4 5 1 2 3")
            print("3 4 5 1 2")
            print("2 3 4 5 1")
            print("1 2 3 4 5")
        else:
            print("Case #{}:".format(jj),"IMPOSSIBLE")
    jj+=1
    t-=1
