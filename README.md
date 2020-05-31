# India Statewise greenhouse gas emissions and rainfall 


**Project developed as part of Data Visualization course at IIIT Hyderabad**



**PURPOSE OF VISUALIZATION**

The purpose of this visualization is to draw the correlation between greenhouse gas emissions and annual rainfall in each state of India and also analyze the condition of states(declining or improved) over the years. This will help the governments of respective states to analyze the situation and regulate the number of industries to maintain the ecological balance. This will also help to study the contribution of industries on greenhouse gas emissions and the effect of greenhouse gases on rainfall.


**DATASET FOR VISUALISATION**

The datasets we plan to visualize are the [Annual Rainfall of states in India](https://data.world/rajanand/rainfall-in-india/workspace/file?filename=rainfall+in+india+1901-2015.csv) and the Annual greenhouse gas emission dataset (available on [GHC platform](http://www.ghgplatform-india.org/economy-wide) India)These are three separate data-sets that have state-wise distribution, we will club them for the years on which data is available and will clean to make it fit for the visualization.
According to the current data, yearly information is available from 2005-2015. This data is good enough to draw the desired conclusion because most of the industrialization occurred in these years.

[Dataset after pre-porcessing](https://drive.google.com/open?id=1fL5hN7Vda4ovFjmVOvWoAfutVB7vGFAU
)


**ANALYSIS**

We presented the main map showing statewide rainfall trends with the intensity of color showing the category of the rainfall. To draw a better conclusion between various emissions like Carbon, No2, CH4, and Rainfall we presented the data from 2005 to 2015 for each state on hover on that state. With the use of a slider, the user can change the years and check the comparison of rainfall between states. There is a linked bar chart for the rainfall and Nitrogen, CH4 emission, etc. Users can have a better comparison with the map and bar charts of different emissions and compare the data more accurately between different states. The user can compare data between different states based on the particular parameters also for each year. The slider also brings a change in the bar graph. The same code can be extended for different visualizations like Growth of COVID-19 in different states over the days or For Growth of COVID-19 across all the countries etc.


**INSTRUCTIONS**


1. The project uses Python3. All the requirements are specified in the
folder with the name requirements.txt.

2. To install the required modules
pip install -r requirements.txt

3. To run the application
Use bokeh serve --show Int-elligence (folder_name)
