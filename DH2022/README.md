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
pip install "thefuzz[speedup]"
pip install "gensim"
pip install "nltk"
```

## Download data