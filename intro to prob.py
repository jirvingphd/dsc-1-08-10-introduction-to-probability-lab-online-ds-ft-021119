# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:06:30 2019

@author: james
"""

import numpy as np
np.random.randint(1,7) # you will get a random value between 1 and 6. See how it changes when you rerun
# from Collections import counter

np.random.seed(12345) # to make sure there is no randomness
roll_dice = set(range(1,7))
event = set([5,6])


dice_10 = np.random.randint(1,7,size= 10)
dice_1k = np.random.randint(1,7,size= 1000)
dice_1m = np.random.randint(1,7,size=1000000)
dice_100m = np.random.randint(1,7,size=1000000000)


b=dice_1k[np.where(dice_1k==(5 or 6))]
c=dice_1k[np.where(dice_1k==5)]
d=dice_1k[np.where(dice_1k==6)]
