# distributor

## Overview

This directory contains the script and libraries for the general reject-accept distributor.

## Running

Running `distributor.py` is as simple as:

```bash
$ python distributor.py --options
```

## Files

| File | Description |
| ---- | ----------- |
| `distributor.py` | The Python script to be run, that produces the distributed random numbers. |
| `distributor_lib.py` | The module containing the functions necessary for the operation of `distributor.py`. |
| `distributor_plot.py` | The module containing all the plotting functions used to histogram the produced random numbers (requires `matplotlib`). |
| `distributor_io.py` | The module containing all the input/output functions used by `distributor.py`, namely writing the distributed random numbers to plaintext and to Excel spreadsheet (if `xlwt` is installed). |
| `str_to_func_lib.py` | The module containing the function that takes a string as input and turns it into an anonymous (or lambda) function that evaluates the mathematical expression given by the user as an argument. Thi has been separated as a module so that the nasty but unnecessary `from numpy import *` and `from scipy.special import *` only affect the one function, `str_to_func()`. |

Subdirectories are the default locations to save data and graphs, respectively.

## Options

| Options | Required | Description |
| ------- | -------- | ----------- |
| `func` | Yes | The main compulsory positional argument; a string that when evaluated is a valid Python mathematical expression with "x" as the operand, e.g. "sin(x)", "gamma(x)" etc. |
| `-r` or `--range` | Yes | The range to produce the random numbers from and to. Enter as valid Python tuple within string, e.g. "(1,2)", "(-e, pi)". Accepts basic mathematical constants, e.g. e, pi.
| `-p` or `--plot` | No | Plot histograms of the produced distributed random numbers to specified file (requires `matplotlib`) |
| `-o` or `--output` | No | Output the produced distributed random numbers to specified file. |
| `-x` or `--excel` | No | Output the produced distributed random numbers to specified file as Excel spreadsheet. |
| `-n` or `--num` | No | The number of initial random numbers to generate. As this uses the reject-accept method, some of these are rejected and the actual nunber of random numbers is less than this. If you want to have a fixed number of random numbers produced, use `-f` or `--fixnum`. |
| `-f` or `--fixnum` | No | Use this flag if you want to produce a fixed number of random numbers, as given by the `-n` or `--num` argument.
| `-t` or `--timed` | No | Print processor timing information. |

## Requirements

The plotting option, `-p` or `--plot`, requires `matplotlib`, which can be installed via `pip` with:

```bash
$ sudo pip install matplotlib
```

The print to Excel spreadsheet option, `-x` or `--excel`, requires `xlwt`, which can be installed via `pip` with:

```bash
$ sudo pip install xlwt
```