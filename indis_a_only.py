#program sa pemet nou jwenn tout index yon eleman nan yon chenn
#9
n="captain america is a superhuman"
n2=[]
indis="a"
for i in range(len(n)):
    if n[i]==indis:
        n2.append(i)
print(n2)