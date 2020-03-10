#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__     = ['Benjamin Dillenburger','Demetris Shammas','Mathias Bernhard']
__copyright__  = 'Copyright 2019 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<dbt@arch.ethz.ch>']

import math

def grid_set_values_at_borders(grid, value):
    for i in range(grid.nx):
        for j in range(grid.ny):
            for k in range(grid.nz):
                if (x==0 or x==grid.nx-1):
                    grid.set_value_at_xyz(value,i,j,k)
                elif (y==0 or y==grid.ny-1):
                    grid.set_value_at_xyz(value,i,j,k)
                elif (z==0 or z==grid.nz-1):
                    grid.set_value_at_xyz(value,i,j,k)

def grid_set_values_sinusoids(grid, freq_x, freq_y, freq_z):
    for i in range(grid.nx):
        for j in range(grid.ny):
            for k in range(grid.nz):
                vx = math.sin(i/grid.nx * freq_x)
                vy = math.sin(j/grid.ny * freq_y)
                vz = math.sin(k/grid.nz * freq_z)
                v = utils_math.map((vx+vy+vz),-3.0,3.0,-1.0,1.0)
                grid.set_value_at_xyz(v,i,j,k)
