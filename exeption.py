#!/usr/bin/python3

def main():
    try:
        fh=open('lines.txt')
    except IOError as e:
        print('couldnot open file',e)
    else:
        for line in fh: print(line.strip())

if __name__=="__main__":main()
