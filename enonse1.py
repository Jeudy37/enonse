from operator import index
adres=input("antre yon adress ip : ")
ip= adres.split(".")
adr="".join(ip)
sum=[]
som=0
for i in adr:
    sum.append((i))  
kalkil=[int(x) for x in sum]
for i in kalkil:
    som= som+i
#full= som * kalkil[0]   
print(som)
  