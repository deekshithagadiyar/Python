'''
Problem 2:
Problem Description
Rotate a given String in the specified direction by specified magnitude.
After each rotation make a note of the first character of the rotated String, After all rotation are performed the accumulated
first character as noted previously will form another string, say FIRSTCHARSTRING.
Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.
If yes print "YES" otherwise "NO". Input
The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains
character d[i] denoting direction and integer r[i] denoting the magnitude.
Constraints
1 <= Length of original string <= 30
1<= q <= 10
Output
YES or NO
Example 1
Input
carrace
 3
 L 2
 R 2
 L 3
Output
NO
'''
string=input()
no_rotation=int(input())
rotation_list=[]
for _ in range(no_rotation):
    rotation_list.append(input().split())
fchar_string=''
for r_type,nor in rotation_list:
    nor=int(nor)
    if r_type=='L':
        fchar_string+=(string[nor:]+string[:nor])[0]
    elif r_type=='R':
        fchar_string+=(string[nor*-1:]+string[:len(string)-nor])[0]
    print(fchar_string)
substring_list=[]
for index1 in range(1,len(string)+1):
    for index2 in range(index1,len(string)+1):
        if len(string[index1-1:index2])==len(fchar_string):
            substring_list.append(string[index1-1:index2])
for substring in substring_list:
    if sorted(fchar_string)==sorted(substring):
        print('YES')
        break
    else:
        print('NO')
