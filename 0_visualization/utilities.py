'''
This is a help script
'''

import os
import pandas as pd
import numpy as np

import plotly as pl
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
from plotly.graph_objs import *
import plotly.plotly as py
import cufflinks as cf
init_notebook_mode(connected=True)
from IPython.display import Image

######################################

print ("plotly ",__version__)


def lay(plot= ' ', xaxis = ' ', yaxis = ''  ):
    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(
                family='sans-serif',
                size=25,
                color='#E7E7E7'
            ),

        title= plot,
    xaxis=dict(
            title= xaxis,
            titlefont=dict(
                family='Courier New, monospace',
                size=40,
                color='##E7E7E7'
            )
        ),
    yaxis=dict(
            title= xaxis,
            titlefont=dict(
                family='Courier New, monospace',
                size=40,
                color='##E7E7E7'
            )
        )
                )
    return(layout)

## make categorical values
def category (a):
    if a >= 90:
        return (1)
    else:
        return (0)

def sectomin(x):
    return (x/60)       
