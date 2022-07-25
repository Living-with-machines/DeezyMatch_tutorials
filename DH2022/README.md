# DH2022: Digital Humanities conference

- [Installation and setup](#installation-and-setup)
- [Tutorials](#tutorials)
- [Credits and re-use terms](#credits-and-re-use-terms)

---

## Installation and setup

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

Clone the DeezyMatch tutorials repository:
```bash
git clone https://github.com/Living-with-machines/DeezyMatch_tutorials.git
```

**Download data:**

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

---

## Tutorials

We have prepared three sets of tutorials for the DH2022 conference:
- [DM_101](DM_101): Dummy string matching and ranking between a small number of queries and candidates
- [ocr_with_w2v](ocr_with_w2v): Fuzzy string matching and ranking between:
    - queries: tokens in English containing OCR errors
    - candidates: list of words in the English language
- [libyan_gazetteer](libyan_gazetteer): Toponym matching and ranking between:
    - queries: toponyms obtained from the Heritage Gazetteer of Libya (HGL)
    - candidates: list of toponyms (and alternate names) belonging to places in current-day Libya, from Geonames.

---

We start with the [DM_101](DM_101) tutorial:

1. Go to [DM_101](DM_101) directory:

```bash
cd DH2022/DM_101
```

2. Open Jupyter Notebook: `tutorial_101`.

Here, we use already created datasets (i.e., queries/candidates/pairs) for training and using a DeezyMatch model. This includes training a pair classifier and using the trained model for candidate ranking.

---

We continue with the [ocr_with_w2v](ocr_with_w2v) tutorial:

1. Go to [ocr_with_w2v](ocr_with_w2v) directory:

```bash
cd DH2022/ocr_with_w2v
```

2. Open Jupyter Notebook: `tutorial_ocr_w2v`.

Here, we use already created datasets (i.e., queries/candidates/pairs) for training and using a DeezyMatch model. This includes training a pair classifier and using the trained model for candidate ranking.

These datasets were created in Jupyter Notebook: `prepare_dataset`. 

---

Next, we go to [libyan_gazetteer](libyan_gazetteer) tutorial:

1. Go to [libyan_gazetteer](libyan_gazetteer) directory:

```bash
cd DH2022/libyan_gazetteer
```

2. Open Jupyter Notebook: `tutorial_hgl`.

Similar to the previous tutorial, we use already created datasets (i.e., queries/candidates/pairs) for training and using a DeezyMatch model. This includes training a pair classifier and using the trained model for candidate ranking.

These datasets were created in Jupyter Notebook: `prepare_dataset`. 


## Credits and re-use terms

GeoNames Gazetteer extract files is licensed under a Creative Commons Attribution 4.0 License, see https://creativecommons.org/licenses/by/4.0/.

Heritage Gazetteer of Libya (HGL) is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
