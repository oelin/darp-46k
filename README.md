# DARP 46K

A dataset consisting of 46K MCPP problems with solutions found by DARP.

<img src='https://github.com/alice-st/DARP/raw/main/images/STC.png'>

## About

DARP is an efficient algorithm for multi-agent coverage path planning (MCPP). This dataset contains 46537 examples of MCPP problems on a 10x10 map with solutions found by DARP after a maximum of 100 iterations. Each problem involves four agents and 10 randomly positioned obstacles. The solutions are given as bitmaps denoting the allocated areas for each agent. We recommend using the provided [extraction script](./scripts/load.py) to extract the dataset.


## Extracting The Data

The dataset is encoded in a compressed, non-standard format optimized for the particular information required about each example. We have provided an extraction script which can be used to load the dataset easily.

```py
>>> from darp_46k import extraction
 
>>> dataset = extraction.extract_dataset()
```
