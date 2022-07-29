from operator import index


#program sa pemet ou adisyone tout index yon karakte nan on chenn
# 8
n="captain america Alvia"
n2=[]
va='a'
add=0
for i in range(len(n)):
    if n[i]== va:
         n2.append(i)
for i in n2:
    add+=i      
print(add)