# Collocation Networks

For my presentation at SDSS I depended upon Wordij to generate a collocation network for the text I was treating — I was demonstrating the focus on a single text that has emerged recently in corpus stylistics — along with its companion application, Visij. In the days leading up to the conference, I looked around for a Python equivalent and was, honestly, surprised not to be able to find anything. In these days following the conference, I have looked some more and I have still been unable to find anything. The only software I have seen is a part of the Lancashire group's efforts: they also produced LancsBox and I signed up for the course. (There's something I can do in the weeks ahead!)

I found myself thinking about writing my own script, or scripts to do it. As I have thought about it, I have imagined the mechanics would looks little like what is described below.

Just now, as I was writing this, I realized I have looked mostly for "Python collocation network" but I have not looked for scripts that are simply "Python collocation". I also realized that I could potentially either use, or base my own work, on the functionality built into the NLTK's `ngram` modules.


## Build Notes

The "window" is the same thing as an ngram, but reducing the gram to simply the relationship between the base word, here the word furthest to the right, and its collocates. **Question**: it is at all interesting how close or far the words are? That is, do we want to know if a word is three steps or four steps away? **Tentative answer**: no.

So, we are keeping track of word pairs, counting the number of times two words are within some distance of each other. We have:

    base, collocate, frequency

We can store that as a tuple or as a Pandas dataframe (which is essentially a Numpy array?).

## Some Examples

A search for "python collocation" turned up Francis Bonds' [HG2051: Language and The Computer](http://compling.hss.ntu.edu.sg/courses/hg2051/). From [http://compling.hss.ntu.edu.sg/courses/hg2051/week09.html], there is the following:

```python
def collocations(words):
    from operator import itemgetter

    # Count the words and bigrams

    wfd = nltk.FreqDist(words)
    pfd = nltk.FreqDist(tuple(words[i:i+2]) for i in range(len(words)-1))

    #
    scored = [((w1,w2), score(w1, w2, wfd, pfd)) for w1, w2 in pfd]
    ## sort according to the score
    scored.sort(key=itemgetter(1), reverse=True)
    return [p for (p,s) in scored]


def score(word1, word2, wfd, pfd, power=3):
    'return the collocation score f(w1,w2)^power/(f(w1)*f(w2))'''
    freq1 = wfd[word1]
    freq2 = wfd[word2]
    freq12 = pfd[(word1, word2)]
    return freq12 ** power / float(freq1 * freq2)
```


Part of a [course][HG2051] being offered by [Francis Bond][fb] at Nanyang Technological University. One the page for the course, he cites Jurafsky and Martin's _[Speech and Language Processing][slp]_ (2009) as well as Chris Manning and Hinrich Schütze's _[Foundations of Statistical Natural Language Processing][fsnlp]_ (1999).

[HG2051]: http://compling.hss.ntu.edu.sg/courses/hg2051/
[fb]: http://www3.ntu.edu.sg/home/fcbond/
[slp]: http://www.cs.colorado.edu/~martin/slp.html
[fsnlp]: http://nlp.stanford.edu/fsnlp/
