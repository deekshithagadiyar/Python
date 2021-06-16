'''
program to print the following pattern
Input
5
output
1    5
 2  4
   3
'''
n=int(input())
if n%2==1:
   for i in range(1,n//2+1):
       print(' '*(i-1),i,' '*(n-i*2),n-i+1,sep='')
   print(' '*(n//2),n//2+1,sep='')
