m={}

def fub(n):
     if n not in m:
        if n <= 2 :
           m[n] =  1
        else:
           m[n] =  fub(n-1) + fub(n-2)

     return m[n]

i=1
while len(str(fub(i))) != 1000:
   i+=1
print(i)
