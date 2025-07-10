# The Single Crystal _GARNET_ project

[![CI](https://github.com/neutrons/garnet/actions/workflows/actions.yml/badge.svg?branch=next)](https://github.com/neutrons/garnet/actions/workflows/actions.yml)
[![codecov](https://codecov.io/gh/neutrons/garnet/branch/next/graph/badge.svg?token=J1ZNHXF6Ml)](https://codecov.io/gh/neutrons/garnet)
[![Documentation Status](https://readthedocs.org/projects/garnet-neutrons/badge/?version=latest)](https://garnet-neutrons.readthedocs.io/en/latest/?badge=latest)

Full documentation available at https://garnet-neutrons.readthedocs.io/en/latest

- [Overview](#overview)
- [Installation](#installation)

## Overview

Single Crystal Graphical Advanced Reduction Neutron Event Toolkit

Garnets are a group of minerals with high symmetry cubic crystal system with space group _Ia-3d_ (#230).
Although they come in many colors, the word comes from a 14th-century Middle English word that has the meaning _dark red_ due to the color of many naturally occurring silicate minerals.
Some rare-earth synthetic garnets has recently served as a useful calibration standard used across several beamlines.

The goal of this project is to combine several amorphous tools from many of the instruments into a user-friendly environment for data reduction.
The scope of this project only covers reduction post-data collection.

Future development may incorporate live data reduction or analysis, but that is not the focus in this effort.

Scope of covered instruments

- TOPAZ
- MANDI
- CORELLI
- DEMAND
- WAND2
- SNAP

The garnet tool will allow users to select single crystal diffraction data from one (minimally white beam) or more (minimally monochromatic beam) orientations, and transform it into a meaningful form.
There exists essential steps of a single crystal data reduction.
These include:

- UB matrix determination and refinement for data reduction and experiment planning
- Peak integration and corrections for structure refinement
- Reciprocal space reconstruction for visualization and analysis
- Order parameter tracking and event filtering analysis

Data processing will be based on Mantid and use PyQt for the application.

## Getting Started

To get started, you will need to have [pixi](https://pixi.sh) installed.
If you don't have it installed, you can follow the instructions on the [pixi installation page](https://pixi.sh/docs/installation).

Clone the repository and setup the environment

```bash
git clone git@github.com:neutrons/garnet.git
cd garnet
pixi install
```

Installing, you can run Garnet from the project root directory as:

```bash
$ pixi shell
$ garnet

# or simply
$ pixi run garnet
```

To run Garnet tests from the project root directory:

```bash
pixi run test
```

Several pixi [tasks](https://pixi.sh/latest/workspace/advanced_tasks) are available for convenience,
and can be listed by running:

```bash
pixi task list
```
