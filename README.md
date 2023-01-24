# DARP 46K

A dataset consisting of 46K MCPP problems with solutions found by DARP.

<img src='https://github.com/alice-st/DARP/raw/main/images/STC.png'>


## About

DARP is an efficient algorithm for multi-agent coverage path planning (MCPP). This dataset contains 46537 examples of MCPP problems on a 10x10 map with solutions found by DARP after a maximum of 100 iterations. Each problem involves four agents and 10 randomly positioned obstacles. The solutions are given as bitmaps denoting the allocated areas for each agent.


## Installation

```sh
$ pip install git+https://github.com/oelin/darp-46k
```

## Loading The Data

The dataset is encoded in a compressed, non-standard format optimized for the particular information required about each example. Nonetheless, it can be easily loaded using the `load_data()` method.


```py
>>> import darp_46k
 
>>> data = darp_46k.load_data()
```

Each example in the dataset is a 3-tuple containing the following:

* `agent_coordinates` - a list of `(y, x)` coordinates denoting the initial positions of each agent on the map.
* `obstacle_coordinates` - a list of `(y, x)` coordinates denoting the positions of each obstacle on the map.
* `solutions` - a NumPy array of bitmaps denoting the allocated area for each agent.
