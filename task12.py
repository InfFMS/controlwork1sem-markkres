def F(n):
    mas=[]
    for i in range(1, int(n**0.5)+1,1):
        if n%i==0:
            mas.append(i)
            if i!=int(n**0.5):
                mas.append(n//i)
    mas.sort(reverse=True)
    mas.pop(0)
    mas.pop(-1)
    if len(mas)<5:
        return 0
    else:
        return mas[4]
i=300000001
count=0
while True:
    if F(i)>0 and count<5:
        print(i)
        count+=1
    i+=1
