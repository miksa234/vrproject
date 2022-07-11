# FILM SCRIPT

Welcome, my name is Milutin Popović and I will introduce you to a project I
have been working on in this semester involving Networks and Python.

Python is known to be an easy to use, simple to learn programming language
used by hobbyists, software developers, scientists and students like me. To
save time and all in all make our lives easier while coding, we fall back to
using what are called python packages. These packages are essentially already
written out code by a group of people or one person and mostly made available
for the public to use without any actual restrictions. This allows us to use
well thought out and optimized code without actually needing to write it
ourselves.


So, if we were to write a python program and use some of these packages, we
would call our program dependent on these packages. On the other hand the
package that we are using is not dependent on the program we are writing it,
at least not yet. And like our dummy program every single package might also
depend on some other package or multiple packages.

To get dependency information of each package we resort to the Python Package
Index, which is the official repository for python packages. Mapping packages
as nodes and their dependency information as directional links to these nodes
we can represent this information in a complex network/graph with nodes and
directional links. The network layout is structured in a pyramid scheme in such
a way that the nodes with high degree are at the top, while low degree nodes
are tend to the bottom.

Like most complex networks on the internet this is a scale
free network where a lot of the times ''rich get richer'' scenario comes into
play. Older, and more popular packages tend to be used frequently than newly
created ones. Never the less this does not not restrict us from finding new information

With a little bit of creative thinking we can reconstruct time dependent
data. By this I mean we can reconstruct the same exact network for each and
every month from the date the Package Index was created, around 2005
to this year 2022. An interesting thing to look here are the rising
stars, created in last few years that have gained a large number of
in dependencies/in degrees in a short period of time. These are shown in the picture here.
Some of these packages are already well recognized in the data science/
machine learning community like keras and torch, and some other packages
are tending to replace older packages showing a logarithmically flattening
curve. An example of this would be 'hpptx'. Now we can take a look how over
the years they have quite quickly risen through the levels of our network
layout to being the top nodes.

Indeed you might want to keep an eye on these packages, since they can quite
easily replace some of the older flattening packages in the community and
represent based on the analysis that we have done, all in all quite solid projects.
