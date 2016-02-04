#!/usr/bin/python3

import random
def main():
    user_input = input("enter text or paragraph:")
    user_input = user_input.lower();
    if type(user_input)== str:
        array = list(user_input)
        print random.choice(array)

if __name__=="__main__":main()
