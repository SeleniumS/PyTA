# Python on Mac

First, in case you didn't know it, the modern Mac operating system -- the one they insist keeping as X (as in OH ESS EX, now, "eleven") -- is really just a pretty face for Unix. That is, it is POSIX-compliant, which is probably something that will never mean much to you, except when you want to extend the functionality of the OS and you discover there is just a lot, a lot of stuff already built for you. 

One of the things that various flavors of Unix, including Linux, have had for a long time are package managers, something the Mac OS now has in the case of the App Store. In brief, a package manager does two things -- well at least these two things worth pointing out here: first, a package manager knows what else you might need for a piece of software to run, and it will go ahead and install it for you, and, second, a package manager will update your software, all of it if you like, with a single click or, in the case of the command line, with a single typed line.

The best package manager I have found to use with the Mac OS, and there are a few, is MacPorts. One important feature of using MacPorts, is that we are going to install a separate version of Python than the one that comes with Mac OS. This is important: if we break anything in our little walled garden of Python, it will have zero effect on the operating system. For the record, MacPorts installs its walled garden at `/opt/local`. (Understanding Unix paths, as they are called, is for another time.)

This is a workshop with "command line" in the title, and so while I wish the first thing you were doing is getting to the command line, we are going to need to take a slight detour, to the [Mac App Store][] to install Xcode. (If that link works, then the App Store opened for you to the Xcode page. If not, you'll need to open it yourself -- which if you want to feel like you're commandlining it, you can do by typing CMD + Space, which opens Spotlight, and then type in "app" and highlight the App Store app, if it isn't already highlighted, and then hit return. *Badabing*. Once in the App Store, just search for "xcode" and proceed as usual.)

Here's everything you need to do, in the order you need to do it, using MacPorts as your basis. Please note this assumes that everything you need to do is in the most recent version of Python, which as of this date is Python 3.4.

First, install Xcode. (Workaround in the offing.)

Second, install Xcode command-line tools. First, this:

    xcode-select --install

And, then, you'll need to do this: 

    sudo xcodebuild -license

Third, download and install the MacPorts base package.

Fourth, once the base package is installed, run:

    sudo port selfupdate

Now, we need to install Python and the various libraries. The basic setup is:

    sudo port install python34
    sudo port install py34-numpy
    sudo port install py34-scipy
    sudo port install py34-matplotlib
    sudo port install py34-pandas
    sudo port select --set python python34

If you would like the option of using *Jupyter* notebooks:

    sudo port install py34-ipython
    sudo port select --set ipython py34-ipython
    sudo port install py34-jupyter

If you're interested in doing text analytics, then you'll probably find the following libraries useful. (Please note that the first line below is a workaround to keep NLTK from installing Python 2.)

    sudo port install xorg-xcb-proto +python34
    sudo port install py34-nltk

If you would like to add R to your arsenal of weapons and to have it work within Jupyter notebook:

    sudo port install R
    sudo port install py34-zmq

Then, in R, using sudo:

    install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
             repos = c('http://irkernel.github.io/', 
             getOption('repos')))
    
    IRkernel::installspec()


[Mac App Store]: http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12