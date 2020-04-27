''' To Do
1. Add more data from IMDB database.(Gross, language, )


Fetching more data from OMDB API
apikey=2be1b857<br>
Example Request :  http://www.omdbapi.com/?i=tt3896198&apikey=2be1b857
Returns JSON

Action Plan:
1. Load your ratings csv and get all IMDB ids
2. using urllib.request urlopen to fetch/get data from OMDB API
3. Using JSON module to actually parse this data.
4. Add/Merge/Join/Concatenate back to original Dataframe.
'''

import pandas as pd

pd.set_option('display.max_columns', 100)
import json
from urllib.request import urlopen

API_Key_OMDB = '2be1b857'
# Lets first read the existing csv to grab the film ids

data_exist = pd.read_csv('../Data/imdb_ratings_april_2020.csv', engine='python', index_col=0)

# filtering just films using .loc indexer
film_filter = (data_exist['Title Type'] == 'movie')

# Film data
data_film = data_exist.loc[film_filter]

# Lets get the IMDB film IDs in a list

index_interest = data_film.index.to_list()


# Creating url request for the API with movie IDs in the form http://www.omdbapi.com/?i=<IMDB ID>&apikey=2be1b857
# Using urlopen.read to fetch the JSON

# Write a function that just gets the dictionary keys from JSON and creates a DF
def create_df(API_Key_OMDB):
    '''
    Takes in OMDB key and creates empty dataframe with the required columns taken from json keys
    :param index_interest:
    :return:
    '''
    with urlopen('http://www.omdbapi.com/?i=tt3896198&apikey=' + API_Key_OMDB) as response:
        # fetching the JSON string for item
        source = response.read()
        # loading json string as a python dictionary
        data = json.loads(source)
        new_df = pd.DataFrame.from_dict(data.keys())
        return new_df


empty_df = create_df(API_Key_OMDB)


# Function that adds to this dataframe details of all movies in index_interest

def fetch_data(df, list_IDS, API_Key_OMDB):
    for i, item in enumerate(list_IDS):
        with urlopen('http://www.omdbapi.com/?i=' + item + '&apikey=' + API_Key_OMDB) as response:
            # fetching the JSON string for item
            source = response.read()
            # loading json string as a python dictionary
            data = json.loads(source)
            print(df.head())
            print(pd.DataFrame.from_dict(data).head())
            #df = pd.concat([df,pd.DataFrame.from_dict(data)])

    #print(df.info())
    #print(df.head())

fetch_data(empty_df, index_interest[:2], API_Key_OMDB)