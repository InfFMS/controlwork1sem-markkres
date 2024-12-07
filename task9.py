def F(a,b):
    if b==0:
        return 0
    elif a>b:
        return F(a-1,b)+b
    elif a<=b and b>0:
        return F(a,b-1)+a
print(F(7,8))
