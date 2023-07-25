#!/usr/bin/env python
# coding: utf-8


import requests
import datetime
from dateutil.relativedelta import relativedelta 
import zipfile
from zipfile import BadZipFile
import os
import io


#Download and extract the number of complete months according to parameter
def dl_extract(num_mos):
    #create the url list oaf the last 6 months available
    url_list = []
    for n in range (1, num_mos+1):
        date = datetime.date.today() - relativedelta(months=n)
        url = f'https://s3.amazonaws.com/tripdata/{date.year}{str(date.month).zfill(2)}-citibike-tripdata.csv.zip'
        url_list.append(url)

    #create folder called citibike_data if does not exist
    if not os.path.exists('citibike_data'):
        os.mkdir('citibike_data')
        
    #Pull the zip files and unzip them
    for url in url_list:
        url_split = url.split('/')
        filename = str(url_split[-1])
        req = requests.get(url)
        try:
            z = zipfile.ZipFile(io.BytesIO(req.content))
            z.extractall('citibike_data')
            print(f'Success! Downloaded and Extracted {filename}')
        except BadZipFile:
            print(f'no zip file exists for {filename}')

    print('Download and extraction complete')


dl_extract(3)