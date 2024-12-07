def F(n):
    mas=[]
    for i in range(1, int(n**0.5)+1,1):
        if n%i==0:
            mas.append(i)
            if i!=int(n**0.5):
                mas.append(n//i)
    return mas
for i in range(174457,174506,1):
    if len(F(i))==4:
        print(F(i)[2], F(i)[3])
