
# coding: utf-8

# # Download cancer-data from figshare
# 
# The latest figshare data is available at https://doi.org/10.6084/m9.figshare.3487685.

# In[1]:

import os
import mimetypes
from urllib.request import urlretrieve

import pandas
import requests


# In[2]:

# Specify the figshare article ID
figshare_id = 3487685


# In[3]:

# Use the figshare API to retrieve article metadata
url = "https://api.figshare.com/v2/articles/{}".format(figshare_id)
response = requests.get(url)
response = response.json()


# In[4]:

# Show the version specific DOI
response['doi']


# In[5]:

# Make the download directory if it does not exist
if not os.path.exists('download'):
    os.mkdir('download')


# In[6]:

for file_info in response['files']:
    # Download file
    url = file_info['download_url']
    name = file_info['name']
    print('Downloading {} to `{}`'.format(url, name))
    path = os.path.join('download', name)
    urlretrieve(url, path)
    
    # Export compressed files to xzipped pickles
    type_, encoding = mimetypes.guess_type(name)
    if type_ == 'text/tab-separated-values' and encoding:
        print('  - converting `{}` to a pickled dataframe'.format(name))
        df = pandas.read_table(path, index_col=0)
        bare_path = path.rsplit('.tsv', 1)[0]
        pkl_path = bare_path + '.pkl'
        df.to_pickle(pkl_path)

