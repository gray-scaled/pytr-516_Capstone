#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd

def process_rawdata(file):
    #read in file, group by station id in start and end
    df = pd.read_csv('citibike_data/'+file, low_memory=False)
    
    #group by start and end station id. lat and lng data is specific to the dock so there is more than one latitdude and longitude per station. 
    #For mapping purposes, I averaged the latitudes and longitudes separately.
    df_starts = df.groupby('start_station_id', as_index=False).agg({'ride_id':'count', 'start_lat':'mean','start_lng':'mean'})
    df_ends = df.groupby('end_station_id', as_index=False).agg({'ride_id':'count', 'end_lat':'mean','end_lng':'mean'})   

    #rename the columns
    df_starts.rename(columns={'start_station_id':'station_id', 'ride_id':'ride_count', 'start_lat':'lat', 'start_lng':'lng'}, inplace=True)
    df_ends.rename(columns={'end_station_id':'station_id', 'ride_id':'ride_count', 'end_lat':'lat', 'end_lng':'lng'}, inplace=True)
    
    #concatenate the starts and ends, then groupby station
    df_list = [df_starts, df_ends]
    df_startend = pd.concat(df_list)
    df_merged = df_startend.groupby('station_id', as_index=False).agg({'ride_count':'sum', 'lat':'mean','lng':'mean'})
    df_merged.sort
    
    #check for folder and create it, save to csv
    if not os.path.exists('processed_data'):
        os.mkdir('processed_data')
    df_merged.to_csv('processed_data/PROCESSED_'+file)

    
#create file list
file_list = []
[file_list.append(csv) for csv in os.listdir('citibike_data/') if 'citibike-tripdata.csv' in csv]
file_list.sort()


#list comp for processing data

for file in file_list:
    print (f'Processing {file}')
    process_rawdata(file)
    print(f'Finshed {file}')