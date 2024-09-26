'''
JavaScript Methods	              Python Methods
str.indexOf(searchValue)	      str.find(sub)
str.includes(searchString)	      'sub' in str
str.lastIndexOf(searchValue)	  str.rfind(sub)
str.startsWith(searchString)	  str.startswith(prefix)
'''
text = 'Py' 'thon'

print(text)  # Output: Python
print(text.swapcase())  # Output: pYTHON
print([c for c in text]) # Output: ['P', 'y', 't', 'h', 'o', 'n']
reversedList = [c for c in text]
copyList = reversedList[:]
reversedList.reverse()
print(reversedList)
print(''.join(reversedList))  # Output: nohtyP
print(copyList[::-1]) # Output: ['n', 'o', 'h', 't', 'y', 'P']

# reversed(text) returns an iterator, so we need to convert it to a list first
print("".join(reversed(text))) # Output: nohtyP

for i in reversed(text):
    print(i, end=',')  # Output: nohtyP
else:
    print()

text2 = '   Python   '
trimmedText = text2.strip()

print(text2.find('P'))
print(trimmedText.startswith('Py'))
