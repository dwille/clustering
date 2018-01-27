#!/usr/bin/env python

# k-means.py
# Purpose:
#   Test k-means clustering with some (artificial) particle data to find
#   "clusters" of particles. Particle parameters to be studied include
#   position, velocity, and force.

import numpy as np
import matplotlib.pyplot as plt


### Initialize "fake" particle data ###
# To start, look at a two-dimensional grid of (nx,ny) particles in a domain of
#  size Lx,Ly

Lx = 1.
Ly = 1.
nx = 10.
ny = 10.

dx = Lx / nx
dy = Ly / ny

x = 0.5*dx + np.arange(nx)*dx + 0.01*np.sin(np.pi*np.arange(nx)/nx)
print(x)


plt.figure()
plt.plot(x, np.ones_like(x), 'o')
plt.savefig("tmp.png")
