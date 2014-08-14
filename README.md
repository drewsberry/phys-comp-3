# phys-comp-3

## Computational Physics, Exercise 3: Random Numbers and Monte Carlo

This repository contains the code for Exercise 3 of Computational Physics 301, on random number generation and distributions and Monte Carlo simulation.
The contents of the code is split in two:

* Generating random numbers following a particular distribution using:
	* an analytic inversion method, and
	* a _reject-accept_ method (conceptually similar to standard Monte Carlo techniques).
* Simulating the distribution of gamma rays, produced by the decay of a beam of unstable nuclei, detected in a nuclear physics experiment.

This branch contains the actual Python code used to produce the program.

# Directories

| Directory | Description |
| --------- | ----------- |
| analytic\_sin | This folder contains the code to analytically produce random numbers distributed sinusoidally, by inverting the sine. For more information, see [analytic\_sin/README.md](https://github.com/drewsberry/phys-comp-3/blob/master/code/analytic_sin/README.md). |
| distributor | This folder contains a general program for producing random distributions that follow a given mathematical function, which is input by the user. This uses the reject-accept method. For more information, see [distributor/README.md](https://github.com/drewsberry/phys-comp-3/blob/master/code/distributor/README.md). |
| gamma | This folder contains the code for a small Monte Carlo gamma decay simulator, including some neat visualisations. For more information, see [gamma/README.md](https://github.com/drewsberry/phys-comp-3/blob/master/code/gamma/README.md) |
| reject-accept\_sin | This folder contains the code to produce random sinusoidally distributed numbers using the reject-accept method. For more information, see [reject-accept\_sin](https://github.com/drewsberry/phys-comp-3/blob/master/code/reject-accept_sin/README.md) |
