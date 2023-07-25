
Problem Statement:
What and where are the least used NYC Citibike Stations? After identifying the stations, does mapping shed light on why they are the least used?  Citibike Stations are able to be deployed in a day, so knowing where and possibly why they are least used may help with deciding to move stations.

Solution:
I pulled the last 3 months of ride data and summarized each month by station. I mapped station locations and color coded them by the month they were from or if they were in the bottom 50 for all 3 months. An overlay of all the stations shows the general area of where the stations are in the network of Citibike Stations. This showed the actual stations were near the border of the Citibike network and/or geographic borders, but not evenly distributed at borders.

Technical Solution:
I used the sum of both starts and ends at a station to determine the least used. I used pandas to group by station, while also averaging the latitude and longitude because coordinates were specific to bikes, not the station. I used a histogram to get a general idea of the upper and lower bounds of the ride count, and where most stations fell within that range. I used the folium module because of the ability to interact with the map to see how their location provided information on why they were least used. The map showed how the least used were at the edge of the network and/or near geographic borders. But since it was not uniform along the border, there are definitely other factors affecting station use.  

File Summary:
***RAW Data pulled from Citibike was too big to save in my GitHub repository
Download_Extract_Last_3_Months.py - Pulls last 3 months from Citibike's AWS bucket, to run in Terminal
Download_Extract_Last_3_Months.ipynb - Jupyter Notebook version
Process_Data_From_CSV.py - Processes csvs and saves it to subdirectory, to run in Terminal
Process_Data_From_CSV.ipynb - Jupyter Notebook version
Analyzing_Visualizing_Data.ipynb - Visualizes the data in histograms and map
Processed_Data - Subdirectory containing processed data by month

Contact Info:
Doug Eng
douglaseng.work@gmail.com