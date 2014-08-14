# gamma

## Overview

This directory contains the script for the Monte Carlo detector simulation, as well as a small script to run a pretty and fun interactive visualisation of how clumping forms when points are not properly picked on a sphere.

## Running

To run the main gamma decay simulation, run:

```bash
$ python gamma.py --options
```

To run the Mayavi sphere visualisation (requires `mayavi`), run:

```bash
$ python sphere_mayavi.py
```

## Files

The files are as follows:

| File | Description |
| ---- | ----------- |
| `gamma.py` | The script to run that simulates the gamma decay. |
| `gamma_lib.py` | The module containing all the functions needed by `gamma.py` to simulate the gamma decay. |
| `gamma_plot.py` | The module containing all the functions for plotting the resulting simulation data to graphs (requires `matplotlib`). |
| `sphere_mayavi.py` | The script for running the Mayavi visualisation of the sphere point picking (requires `mayavi`). |
| `sphere_mayavi_lib.py` | The module containing the functions needed by `sphere_mayavi.py` for running the sphere visualisations (requires `mayavi`). |

Subdirectories are the default locations to save data and graphs, respectively.

## Options

The options for `gamma.py` are as follows:

| Option | Description | Default |
| ------ | ----------- | ------- |
| `-r` or `--range` | The size of the detector in meters. Enter as tuple containing two tuples inside string. For instance, `"((-2.5,2.5),(-4.5,4.5))"` would be a detector spanning from -2.5m to 2.5m in the X direction and -4.5m to 4.5m in the Y direction. Note that there should be no spaces in the string. | `"((-5,5),(-5,5))"` |
| `-n` or `--num` | The number of decays to simulate. | 10 million |
| `-s` or `--speed` | The speed that the injected nuclei are travelling at in meters per second. | 2000 m/s |
| `-l` or `--lifetime` | The average liftetime of the unstable nuclei in microseconds. | 520 &mu;s |
| `-xr` or `--xres` | The x-resolution of the detector in centimetres. Used for both binning and smearing the data. | 10 cm |
| `-yr` or `--yres` | The y-resolution of the detector in centimetres. Used for both binning and smearing the data. | 30 cm |
| `-d` or `--distance` | Distance from the point of injection of the unstable nuclei and the detector, in meters. | 2 m |
| `-p` or `--plot` | Plot the resulting simulated data to eps files (requires `matplotlib`). | N/A |
| `-t` or `--timed` | Print processor clock timing information. | N/A |

Note that gamma.py runs fine without any of the optional arguments, as it's set by default to all the values specified in the script.

The `gamma_sphere.py` script has no options.

## Requirements

The script `sphere_mayavi.py` requires `mayavi` to be installed. The easiest way to install `mayavi` on Windows and MacOS is simply to install a fully Python distribution such as Enthought Canopy. On Debian or Ubuntu, you can simply run:

```bash
$ sudo apt-get install mayavi2
```

The plotting option, `-p` or `--plot`, in `gamma.py` require `matplotlib`, which can be installed via:

```bash
$ sudo pip install matplotlib
```
