# Sagittarius

**Empirical interpolators for the distance and proper motions of the Sagittarius Stream**

This Python package provides the necessary tools to query the proper motions (in different Spherical frames) and distances to the Sagittarius Stream. The interpolating functions are created from the median values obtain with different samples:
1. General ([Antoja et al. 2020](https://ui.adsabs.harvard.edu/link_gateway/2020A&A...635L...3A/doi:10.1051/0004-6361/201937145))
2. RR Lyrae only ([Ramos et al. 2020](https://ui.adsabs.harvard.edu/link_gateway/2020A&A...638A.104R/doi:10.1051/0004-6361/202037819)):
    1. Strip: more complete but also less pure
    2. nGC3: more pure but less complete
  
  
## Documentation

All classes and methods/functions are documented so use the python help() function to find out more.


## Installation

This is a Python3 package (*issues may arise if executed with Python2*).

The required dependencies are:
* [numpy](http://www.numpy.org/)
* [scipy](http://www.scipy.org/)


To install it:
1. Clone the Github repository or download the source file
2. cd to the directory
3. Run ```python setup.py install```


## Basic usage

In the folder *TUTORIALS*, you will find examples on how to use the different functions provided.

The main module is *interpolators* and its main function, *sagittarius_properties*, allows to select from within the three different samples, two reference frames ('Galactic' or 'ICRS') and four properties (distance, depth, and the two components of the proper motion).


## Attribution

If you make use of this package for your research, please acknowledge the authors in your work.
