# Lake-Freighter-Tracker

## Description
Living along the shores of Lake Michigan, when walking at lakeside parks I often
see very large lake freighters (ships) on the horizon. I took an interest in 
watching these ships because I remembered as a kid, my uncle would tell me 
stories about working on 1000 foot long ships while he was a fabricator 
at a major shipyard in Sturgeon Bay, WI. 

Soon I started using an application called Marine Traffic to see if I could 
expect any ships on the horizon while I went for my daily walks at the parks.
Eventually the idea came up - could I make a similar application myself? 

This software application allows the user to take historical AIS
(Automatic Identification System) data from https://marinecadastre.gov/ais/
and visualize the travel patterns of the 13 (1000) foot long ships operating
on the Great Lakes. 

Ultimately, I learned a few interesting things with this project such as creating 
a web app in Streamlit, creating and managing a data frame in pandas, 
and using the very cool map tools offered by Plotly. 

## Installation
Get repo from https://github.com/rgm-27/Lake-Freighter-Tracker

Install the following files using PIP install in terminal: 
> pip install streamlit

> pip install pandas

> pip install plotly_express

## Usage
1. From terminal launch program with streamlit run "Lake Freighter Tracker.py"
2. Obtain "points" data file from https://marinecadastre.gov/ais/
3. Follow prompts within program (see additional info below)

![image](https://user-images.githubusercontent.com/118615143/202866028-108546c5-3485-4ee2-a2a6-27ae540f82cb.png)
Main application page

![image](https://user-images.githubusercontent.com/118615143/202866367-151db13d-5dd2-4397-abe5-4282760c2341.png)
Drag&drop .csv file from https://marinecadastre.gov/ais/
If error is generated saying the file is too large, try this when launching from terminal:  \
(streamlit run "Lake Freighter Tracker.py" --server.maxUploadSize 200) Note: allows up to 200mb file upload now

![image](https://user-images.githubusercontent.com/118615143/202866409-cc5ede11-4f04-4d05-8d44-c3ea06ad2449.png)
Moving to the "Plot" tab, you can now display positional data from the uploaded file  \
Using the far left drop down will allow you to select from the different ships 

![image](https://user-images.githubusercontent.com/118615143/202866574-b96cbbf5-3c35-46ee-aa00-8119cb0fe48c.png)
Using your mouse wheel, you can zoom in on the map to obtain more detail

## Future 
I am sure I will come back to this project to make minor fixes and possibly add other features 












