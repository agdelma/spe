[![PyPI version](https://badge.fury.io/py/spens.svg)](https://badge.fury.io/py/spens)

`spens` is a simple python package that does one thing: loads an ascii .spe file containing neutron scattering (NS) from disk and return `numpy` arrays containing the wavevector (Q), energy (E), scattering intensity (S) and error (ΔS).

## Supported Python Versions
Python >= 3.6 (for f-strings)

## Installation
To install via pip:

    pip install spens

Or from within a notebook:

```python
import sys
!{sys.executable} -m pip install spens
```

## Usage
The library implements a single function `load_spe` which takes the filename of a `.spe` file and return `numpy` arrays.

```python
import spesns
import numpy as np

# load the data
Q,E,S,ΔS = spe.load_file(f'/path/to/scattering/file.spe')

# create meshes for plotting
Emesh,Qmesh = np.meshgrid(E,Q)
```

## Support

The creation of this software was supported in part by the National Science Foundation under Award Nos. DMR-1808440 and DMR-1809027.

[<img width="100px" src="https://www.nsf.gov/images/logos/NSF_4-Color_bitmap_Logo.png">](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1808440)

