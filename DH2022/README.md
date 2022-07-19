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
