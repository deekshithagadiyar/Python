'''
program to print the following pattern
       1
     2 1 2
   3 2 1 2 3
 4 3 2 1 2 3 4
'''
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),*range(i,1,-1),*range(1,i+1),sep='')
