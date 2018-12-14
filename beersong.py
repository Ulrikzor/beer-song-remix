"""
Remix of the beer song, from the tutorial book 'Head First Python', by Paul Barry. Funny song, great book (so far).

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
            time.sleep(1)    
    except ValueError:
        print("Only accepting integer")
        time.sleep(1)
        print()
        repeat()  
repeat()

word = "bottles"
x = ["No", "more", "bottles", "of", "beer", "on", "the", "wall"]
for beer_num in range(repeat.yo, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    time.sleep(2)
    print(beer_num, word, "of beer.")
    time.sleep(1.5)
    print("Take one down.")
    time.sleep(1)
    print("Pass it around.")
    time.sleep(1)
    print()
    if beer_num == 1:
                    for i in x:
                        print(i)
                        time.sleep(0.15)
                        #Found the cleaner way to print list in range with time delay between prints
    else:
        if (beer_num - 1) == 1:
            word = "bottle"
        print(beer_num - 1, word, "of beer on the wall.")
        time.sleep(2)
    print()
