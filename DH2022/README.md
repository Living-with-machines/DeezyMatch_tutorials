# DH2022: Digital Humanities conference

## Installation

We strongly recommend installation via Anaconda (refer to [Anaconda website and follow the instructions](https://docs.anaconda.com/anaconda/install/)).

* Create a new environment

```bash
conda create -n py39deezy python=3.9
```

* Activate the environment:

```bash
conda activate py39deezy
```

* Install DeezyMatch via [PyPi](https://pypi.org/project/DeezyMatch/):
      
```bash
pip install DeezyMatch
```

* Install other dependencies:

```bash
pip install "thefuzz"
pip install "gensim"
pip install "nltk"
```

:warning: (optional) You can also install `thefuzz[speedup]` which provides a 4-10x speedup in String Matching (reference: https://github.com/seatgeek/thefuzz):

```bash
pip install "thefuzz[speedup]"
```

## Download data

For the `libyan_gazetteer` tutorial, we need to download data from `download.geonames.org` and `slsgazetteer.org` (see [Credits and re-use terms](#credits-and-re-use-terms) for info on licenses). 

```bash
python prepare_dirs.py
```

This will create the following files/directories in `libyan_gazetteer/data`:

```bash
libyan_gazetteer
├── data
│   ├── LY.txt
│   ├── alternateNamesV2.txt
│   └── hgl_data.json
├── inputs
│   └── ... 
└── ...
```

## Credits and re-use terms

GeoNames Gazetteer extract files is licensed under a Creative Commons Attribution 4.0 License, see https://creativecommons.org/licenses/by/4.0/.

Heritage Gazetteer of Libya (HGL) is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.