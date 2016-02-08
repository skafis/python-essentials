import re
text = input("enter text or paragraph to search\n")
find = input("enter the word you want to search\n")
if re.search(find,text):
    print (find + " has been found")
else:
    print("sorry "+find+ " cant be found try another word")
