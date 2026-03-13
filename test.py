def money (a,b,c,d):
    x=0
    while a >= 3:
        a-=1
        b+=1
        a-=1
        c+=1
        a-=1
        d+=1
        x+=3
        if b == 35:
            a+=30
            b-=35
        if c ==100:
            a+=60
            c-=100
        if d == 10:
            a+=9
            d-=10
        if a == 2:
            a-=1
            b+=1
            a-=1
            c+=1
            x+=2
        if b == 35:
            a+=30
            b-=35
        if c==100:
            a+=60
            c-=100
        elif a==1:
            a-=1
            b+=1
            x+=1
        if b==35:
            a+=30
            b-=35
    print (x)
money(77,4,9,3)