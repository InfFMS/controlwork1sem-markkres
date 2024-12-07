n=125**5+25**9-30
res=''
while n>0:
    res=str(n%5)+res
    n//=5
print(res)
col=0
for i in range(len(res)):
    if res[i]=="4":
        col+=1
print(col)
