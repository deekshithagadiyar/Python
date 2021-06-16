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
