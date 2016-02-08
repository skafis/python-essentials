#!/usr/bin/python3

import re
def main():
    while True:
        user_input = input("enter text or paragraph:")
        if re.match(r'[a-zA-Z].*',user_input):
            return print(user_input)
        print("please enter text only")

#    print (user_input)
#    #if type(user_input)== str:
#     #   print ("True")
#    #else:
#    #    print ("False"u)
#
#    array = list(user_input)
#    print (array)
#        #Print random.choice(array)

if __name__=="__main__":main()
