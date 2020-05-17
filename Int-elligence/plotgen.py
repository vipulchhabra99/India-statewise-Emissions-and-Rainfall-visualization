#!/usr/bin/env python
# coding: utf-8

# In[3]:


import geopandas as gpd
import pandas as pd
import json


# In[4]:


datafile = 'data/combined_data.csv'

df = pd.read_csv(datafile)
df = df.drop(columns="Unnamed: 0")
# df.columns = ['state', 'year', 'carbon', 'nitrogen', 'CH4', 'rainfall']
df.head()


# In[5]:


df_state = df[df['state'] == 'Rajasthan']
df_state.head()
    


# In[6]:


from bokeh.plotting import figure
from bokeh.io import output_notebook, show, output_file
from bokeh.models import Slider, HoverTool, CustomJS


# In[43]:


def generate_line(state):
    plot = figure(title='GreenHouse Emission VS Rainfall', x_axis_label='Year',plot_width = 700, plot_height = 500)
    import copy
    df_state = copy.deepcopy(df[df['state'] == state])
    years = copy.deepcopy(df_state['year'])
    nitrogen = copy.deepcopy(df_state['nitrogen'])
    rainfall = copy.deepcopy(df_state['rainfall'])
    carbon = copy.deepcopy(df_state['carbon'])
    ch4 = copy.deepcopy(df_state['CH4'])
    ch4 = ch4/400
    carbon = carbon / 10000
    nitrogen = nitrogen/10
    plot.line(years,nitrogen,line_width = 2,line_color='green',legend='Nitrogen')
    plot.line(years,rainfall,line_width = 2,legend='Rainfall')
    plot.line(years,ch4,line_width = 2,line_color = 'yellow',legend='CH4')
    plot.line(years,carbon,line_width = 2,line_color = 'black',legend='Carbon')

#     #plot.line(df_state['year'], df_state['rainfall'], line_width=2, line_color='blue', legend='Rainfall')
#     print(set(df_state['year'][1:]),df_state['nitrogen'])
#     plot.line(set(df['year'][1:]), df_state['nitrogen'], line_width=2, line_color='orange', legend='CH4')
#     plot.circle(set(df['year'][1:]), df_state['nitrogen'], line_width=2, line_color='Red', legend='CH4')
#     hover = HoverTool()
#     hover.tooltips = """
#     <div style=padding=5px>Year:@year</div>
#     <div style=padding=5px>Population:@rainfall</div>
#     """
#     plot.add_tools(hover)
    output_notebook()
    show(plot)


# In[44]:


generate_line('Haryana')


# In[9]:


state_list = list(set(df['state']))


# In[10]:


state_list


# In[49]:


def generate_stackArea(state):
 
    import copy
    df_state = copy.deepcopy(df[df['state'] == state])
    df_dummy = copy.deepcopy(df[df['state'] == state])
    df_dummy['CH4'] = df_dummy['CH4']/2000
    df_dummy['carbon'] = df_dummy['carbon']/50000
    df_dummy['nitrogen'] = df_dummy['nitrogen']/10
    p = figure(title='Comparsion of parameters for '+str(state), x_axis_label='Year', y_range=(0, 3000))
    p.grid.minor_grid_line_color = '#eeeeee'

 

    names = ['carbon','nitrogen','CH4','rainfall']
    p.varea_stack(stackers=names, x='year', color=['#abdda4', '#fdae61', '#d7191c','#2b83ba'], legend_label=names, source=df_dummy)
    p.vline_stack(stackers=names, x='year', color=['#abdda4', '#fdae61', '#d7191c','#2b83ba'], legend_label=names, source=df_dummy)
    p.add_tools(HoverTool(tooltips=[("Carbon", "@carbon"), ("Nitrogen", "@nitrogen"), ("CH4", "@CH4"),("Rainfall", "@rainfall"),("state", "@state")]))
    # reverse the legend entries to match the stacked order
    p.legend.items.reverse()
    output_notebook()
    show(p)


# In[50]:


generate_stackArea('Rajasthan')


# In[3]:


import sys
print(sys.version)
import bokeh
print(bokeh.__version__)


# In[ ]:

