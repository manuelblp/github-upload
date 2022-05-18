import math
from scipy.interpolate import griddata
from scipy.ndimage.filters import gaussian_filter
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import seaborn as sns
"""
fivethirtyeight = [
    "#30a2da",
    "#fc4f30",
    "#e5ae38",
    "#6d904f",
    "#8b8b8b"
  ]
sns.set_palette(fivethirtyeight)
