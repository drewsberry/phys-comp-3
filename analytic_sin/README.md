# analytic\_sin

## Overview

This directory contains the code to produce a random sinusoidally distributed set of random numbers using an analytic inversion method.

## Running

The program can be run with:

```bash
$ python analytic_sin.py --options
```

## Files

| File | Description |
| ---- | ----------- |
| `analytic_sin.py` | The script to be run. |
| `analytic_sin_lib.py` | A (small) module for `analytic_sin.py` containing the definitions for the functions that produce the initial evenly distributed random numbers and analytically convert these random numbers to sinusoidally distributed ones. |
| `analytic_sin_plot.py` | The module used by `analytic_sin` that contains the plotting functions. This requires `matplotlib` to be installed, although `analytic_sin.py` itself will work fine without `matplotlib`, simply informing the user that they will be unable to plot to a graph. |
| `analytic_sin_io.py` | The module used by `analytic_sin` containing all the input/output functions. These include printing the random data to plaintext file and to an Excel spreadsheet (requires `xlwt`)|

Subdirectories are the default locations to save data and graphs, respectively.

# Options

| Option | Description |
| ------ | ----------- |
| `-p/--plot` | Plot to file |
| `-o/--output` | Print the produced random data to specified file. |
| `-n/--number` | The number of random numbers to produce. |
| `-t/--timed` | Print processor timing information. |
| `-x/--excel` | Print the produced random data to specified Excel spreadsheet. Note a limitation in Excel spreadsheets prior to 2007 limits the number of rows to 65,536. |

Note that no arguments need be specified. Giving no arguments does not plot or print output, but works fine.

## Requirements

For plotting, `matplotlib` is required. This can be installed with:

```bash
$ sudo pip install matplotlib
```

For outputting the random data to an Excel spreadsheet, the `xlwt` Python module is required:

```bash
$ sudo pip install xlwt
```