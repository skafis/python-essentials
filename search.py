import re
text = input("enter text or paragraph to search\n")
find = input("enter the word you want to search\n")
output = re.search(find,text)
print (find + " has been found")
