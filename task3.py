def impl(A,B):
    return not A or B
def equ(A,B):
    if A==B:
        return 1
    else:
        return 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F=equ( impl( equ(x,z), ( not y or w)), not(impl(w,z) or impl(x,y)))
                if F==1:
                    print(z,y,x,w)
print("строки по сравнению с таблицей в обратном порядке")                
