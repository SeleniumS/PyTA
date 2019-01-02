# PyTA: Python for Text Analytics

## Introduction

Welcome to the repository for PyTA, which in keeping with Pythonic tradition is pronounced _pie-ta_ ("pie" as in the dessert, and not, as the phonetic spelling might suggest to some, the genre of religious painting). This repo began life as "Useful Python Scripts for Texts," first on [my website] and later as a small repo here on GitHub. As UPST, it was originally constructed for teaching students in an honors academic writing course. Later, the repo got reused for a number of workshops, vestiges of which are present in some of the notebooks, eventually developing into a more general resource.[^1]

As I tell anyone using these materials, please feel free to clone, download, and improve everything and anything in this repo. This is open access scholarship which is modeled on the spirit and practices of open source software development, where everyone can, and does, make an important contribution. Some big, and some bigger than they first appear. (Starting, no matter how small, is always better than not starting.)

The documents and scripts in this repository were developed, and are still in the process of development, not only as a path for you and others to follow, but also as a record of my own progress. Everywhere you look, you will actually see an almost infinite series of contributions from unseen others who have helped me either directly, by responding to questions on fora like [StackOverflow], or indirectly by publishing notes on their blogs or creating repositories like this one. (You can find me on StackOverflow [here].)

# Whython?

As the name of this repository confirms, this repo is founded on Python. There are a number of powerful scripting languages available to scholars interested in computational approaches to their subject(s), each of which has its particular strengths, and each of which also has its peculiarities, confusions, or moments of hair-pulling. For our purposes, I have decided to use Python for one, principled reason: its NLP library, known as the NLTK (natural language toolkit), is remarkably powerful, remarkably easy to use, and used not only by a large number of scholars and scientists but also a diverse range of scholars and scientists, so there is lots of documentation available.[^2]

It should be noted that there are other languages out there, and that they may be either better suited to the kind of work you want to do or to the way your brain works. If you already know you want to work with lots of texts and you are oriented towards statistics, then [R] might be something for you to explore. Similarly, if you are interested in having an interactive web site that works readily with a database of materials, then [Ruby] may be a better choice for you, because of Rails. The same goes for other languages. In general, it's been my experience that the languages are not as hard as getting your brain to think in terms that let you do computation on things like texts which most scholars are used to thinking about in other ways. My journey took me briefly through Perl, before taking up Python. I like Ruby a lot -- it's a beautiful language, but it came down to the NLTK for me and the robustness of some of the other Python libraries. I have used R and liked it.

## Usage

In order to make these scripts as easy to use as possible, they are designed to be run from the command line. In the case of the latter, output can be captured from `stdout` by simply sending the results to a text file of the user's own naming:

```
python pythonscript.py > output.txt
```

Yup, it's just that easy.

## About this repo

Like a lot of open source software, it has two characteristics:

1. it is free to share with others, and
2. it is indebted to more people than I can thank here.

The latter is especially true since I am entirely self-taught when it comes to coding in Python and each of these scripts is the product of a lot of scrutinizing of other scripts and copying of code until I understood how things worked and could write it myself.

As a way to thank my many teachers, I have tried here to comment the scripts as thoroughly as I could, in the hope that I can help others in the same way I was helped.

All of this work is hereby in the [public domain].

[^1]: One of those first workshops was at LSU, where I got paired with the amazing Charles Pence, who has his own [repos here on Github](https://github.com/cpence/). [^2]: Speaking of documentation, the NLTK has a terrific book, _Natural Language Processing with Python_, which is available from O'Reilly both in paper -- I will bring my copy to show -- but if you buy it as an ebook, you get a PDF, an ePub, and a Kindle version associated with your account that you can download at any time. In the mean time, here's a link to the book on the [O'Reilly Store] and the obligatory link to [Amazon]. The authors of the book are also the developers of the NLTK, and, in that open access vein described above, they also maintain a [web version of the book].)

[amazon]: http://amzn.to/1OMa1Gx
[here]: http://stackoverflow.com/users/1457672/john-laudun
[my website]: http://johnlaudun.org/
[o'reilly store]: http://shop.oreilly.com/product/9780596516499.do
[public domain]: http://creativecommons.org/publicdomain/
[r]: https://www.r-project.org
[ruby]: https://www.ruby-lang.org/en/
[stackoverflow]: http://stackoverflow.com
[the book]: http://shop.oreilly.com/product/9780596516499.do
[web version of the book]: http://www.nltk.org/book/
