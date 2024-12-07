def F(n):
    s1=int(str(n)[0])+int(str(n)[1])
    s2=int(str(n)[1])+int(str(n)[2])
    s3=int(str(n)[2])+int(str(n)[3])
    mas=[s1,s2,s3]
    mas.sort()
    return str(mas[1])+str(mas[2])
for i in range(1000,10000,1):
    if F(i)=="1418":
        print(i)
