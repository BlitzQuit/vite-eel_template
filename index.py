# coding: utf-8
import eel
import sys
import time



@eel.expose
def hello():
    print('hello')

@eel.expose
def increment(x) -> int:
    x += 1
    return x;
    


if __name__ == '__main__':#uncomment for dev
    '''if sys.argv[1] == '--develop':
        eel.init('client')
        #eel.start({"port": 3000}, host="localhost", port=8888)
        eel.start({"port":5173},mode="chrome",host="localhost", port=8888)
    else:'''
    eel.init('fdist')#name for the dir name included index.html
    eel.start('index.html')
