#!/usr/bin/python3

import random
def main():
    user_input = input("enter text or paragraph:")
    user_input = user_input.lower();
    print (user_input)
    #if type(user_input)== str:
     #   print ("True")
    #else:
    #    print ("False"u)

    array = list(user_input)
    print (array)
        #Print random.choice(array)

if __name__=="__main__":main()
