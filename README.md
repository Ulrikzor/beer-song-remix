# beer-song-remix
Remix of the beer song program, from the tutorial book 'Head First Python' by Paul Barry.

Just started to learn Python and trying out some of the basic stuff I learned so far. 
The original program prints the whole song, 99 verse in one long print, I wanted it to print it line for line, 
verse for verse and then mimic the same speed I would sing it, kind of like a karaoke machine.

After making the first change I went on to add the opening input(), 
where you're asked how many bottles of beer you got on your wall. Your answer results in how many verses the program will loop.

I then added the response to if your answer is 0 (zero), instead of just closing, it prints: Go to the store and buy some more.
Also added the Try, except ValueError commands, to prevent it from stopping if you respond with anything else than integers.

Finally, I did the thing with the last verse, just to have a different ending to it.
Wanted to code the whole part in just a few lines by putting all the single words into a list and then print it with some kind of 'for x in' combined with a time.sleep interval, but couldn't find a convenient way of doing this.


I'd really appreciate some feedback, I'm new to this and really want to learn. Thanks
        


The Original program: http://python.itcarlow.ie/ed2/ch01/beersong.py
The song: https://www.youtube.com/watch?v=u-lV0vrEWXw
The book: http://shop.oreilly.com/product/0636920036777.do
