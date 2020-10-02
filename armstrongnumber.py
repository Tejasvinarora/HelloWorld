s=0
a=[]
for i in range(100,999):
  p=i
  while i!=0:
    m=i%10 
    s=s+pow(m,3)
    i=i//10
    
  if(p==s):
    a.append(p)
  s=0  
print(a)    
