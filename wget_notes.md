### `wget`

Sometimes CLI tools, like `wget`, are more powerful than GUI tools. The key difference is that GUI tools are easier to use at first, but repetitive tasks are difficult or expensive (in terms of time). CLI tools are a little more difficult at first, but once you have an established collection of them, they are not only easier to use but just plain easier. 

**`wget`** is one of those tools. E.g.:

    % wget -r -l 1 -w 2 --limit-rate=20k https://www.cs.cmu.edu/~spok/grimmtmp/
	
===
	
`wget` is a CLI program that retrieves web content. To my mind, since it can act like a targeted web crawler, it is the single greatest tool available to those looking to gather data/texts. 

Let's look at what it looks like:

wget -r -l 1 -w 2 --limit-rate=20k https://www.cs.cmu.edu/~spok/grimmtmp/
    
* `wget` calls the program
* `-r` (or `--recursive`) turns on recursive retrieving (up to 5 directories deep). 
* `-l 1` (or`--level=1`) keeps the depth to 1.
* `-w 2` gives the amount of time to wait between retrievals. (Two seconds lessens the server load.)
* `--limit-rate=20k` sets the retrieval rate to 20kB/s. (This is being polite in a shared connection setting.)

===

Our test case comes from Zach Isenhower: http://digital.library.okstate.edu/kappler/Vol2/Toc.htm

    http://digital.library.okstate.edu/kappler/Vol2/treaties/bla0736.htm