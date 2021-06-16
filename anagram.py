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
