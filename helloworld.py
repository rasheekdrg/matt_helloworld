#!/usr/bin/python3
''' This test will count from 0 to 100 using __main__. It's written in python3.'''
count = 100
def __main__():
    ''' internal counter, we will count using this value to increase: '''
    count_int = 1;
    while (count_int < count+1):
        if ((count_int % 3 == 0)&(count_int % 5 == 0)):
            print("FooBar")
        elif (count_int % 3 == 0):
            print("Foo")
        elif (count_int % 5 == 0):
            print("Bar")
        else:
            print(count_int);
        
        count_int = count_int+1;
__main__()
