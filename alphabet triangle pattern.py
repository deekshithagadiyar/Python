'''
program to print the following pattern
Input
4
Output
A
AB
ABC
ABCD
'''
n=int(input())
string=''
for i in range(1,n+1):
    string+=chr(64+i)
for i in range(1,n+1):
    print(string[:i]+' '*((n-i)*2)+string[:i])
