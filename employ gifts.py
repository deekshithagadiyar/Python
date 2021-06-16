t=int(input())

for i in range(t):

  n=int(input())

  l=list(map(int,input().split(' ')))

  st='1 '*len(l)

  m=list(map(int,st[:-1].split(' ')))

  for i in range(0,n-1):

     if l[i]>l[i+1] and m[i]<=m[i+1]:

        m[i]=m[i]+1

        for j in range(i,0):

           if l[j-1]>l[j] and m[j-1]<=m[j]:

              m[j-1]=m[j]+1;

           else:

              break

     elif l[i]<l[i+1] and m[i+1]<=m[i]:

        m[i+1]=m[i]+1

  print(sum(m))
