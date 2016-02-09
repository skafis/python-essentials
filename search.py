import re
with open('text.txt')as text:
#    text = f.readlines()
    #text = input("enter text or paragraph to search\n")
    find = input("enter the word you want to search\n")
    for line in text:
        if find in line:
            print (line)
#        print (text)
#        if re.search(r"[find]",text, re.M):
#            print (find + " has been found")
#        else:
#            print("sorry "+find+ " cant be found try another word")
