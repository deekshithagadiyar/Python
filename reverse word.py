'''
Problem 7:
Reverse words in a given String in Python
We are given a string and we need to reverse words of given string ?
Examples:
Input : str = "think career in IT think dlithe"
Output : str = "dlithe think IT in career think"
'''
s=input("str=")
words = s.split()
words = list(reversed(words))
print(" ".join(words))
