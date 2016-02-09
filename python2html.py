#!/usr/bin/python3

#writting to html in python
import webbrowser

def main():
    f=open('hello.html','w')
    message = """head></head>
    <body><p>Hell no</p></body>
    </html>"""
    f.write(message)
    f.close()

    webbrowser.open_new_tab('helloworld.html')

if __name__=="__main__":main()
