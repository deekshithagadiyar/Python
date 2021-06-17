'''
Problem 3:
Stubborn Vowels
In english alphabets there are two types of words, vowels and consonents.You are writing a program to reverse a given string, but the vowels are stubborn to move away from their position. So given a string where the vowels are stubborn,
print what will be word if the entire word is reversed except for the vowels.

Input Format
One string input

Constraints
3<=String length<=10^5

Output Format
Reversed string output

Sample Input 0
missing

Sample Output 0
ngissim

Explanation 0
m + i + ss + i + ng = ng + i + ss + n The string are taken as fragments {m,ss,ng} and the set is reversed and placed
between the vowels.
'''
string=input()
vowels=[]
words=[]
start_index=0

for index in range(len(string)):
   if string[index].lower() in 'aeiou':
      vowels.append(string[index])
      words.append(string[start_index:index])
      start_index=index+1
if string[start_index:]!='':
   words.append(string[start_index:])
words.reverse()
reversed_string=''
for index in range(len(words)):
   if index<len(words):
      reversed_string+=words[index]
   if index<len(vowels):
      reversed_string+=vowels[index]

print(reversed_string)
