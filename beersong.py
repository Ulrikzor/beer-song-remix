"""
Remix of the beer song program, from the tutorial book 'Head First Python', by Paul Barry. Funny song, great book (so far).

The Original program: http://python.itcarlow.ie/ed2/ch01/beersong.py
The song: https://www.youtube.com/watch?v=u-lV0vrEWXw
The book: http://shop.oreilly.com/product/0636920036777.do
"""


import time

def repeat():
    try:
        repeat.yo = int(input("How many bottles of beer on your wall?: "))
        if repeat.yo == 0:
            print("Go to the store and buy some more.")
        elif True:
            print()
            time.sleep(2)    
    except ValueError:
        print("Only accepting integer")
        time.sleep(1)
        print()
        repeat()  
repeat()

word = "bottles"
for beer_num in range(repeat.yo, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    time.sleep(2)
    print(beer_num, word, "of beer.")
    time.sleep(1.5)
    print("Take one down.")
    time.sleep(1)
    print("Pass it around.")
    time.sleep(1)
    if beer_num == 1:
        print("No") 
        time.sleep(0.15) 
        print("more")
        time.sleep(0.15)
        print("bottles")
        time.sleep(0.15)
        print("of")
        time.sleep(0.15)
        print("beer")
        time.sleep(0.15) 
        print("on") 
        time.sleep(0.15)
        print("the") 
        time.sleep(0.15)
        print("wall.")
        """
        Wanted to put all the single words printed above into a list 
        and then print it with som kind of 'for x in' combined with a time.sleep interval
        """
    else:
        if (beer_num - 1) == 1:
            word = "bottle"
        print(beer_num - 1, word, "of beer on the wall.")
        time.sleep(2)
    print()
