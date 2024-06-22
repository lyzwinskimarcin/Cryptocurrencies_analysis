from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os


def get_api_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'EUR'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '381ea747-16ca-4e3e-8c7d-68f2f8ca939c',
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      # print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)


    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')

    return df


def update_data():
    df = get_api_data()
    if not os.path.isfile(r'C:\Marcin Łyżwiński\Projekty portfolio\Web Scraping\Data\APIdata'):
        df.to_csv(r'C:\Marcin Łyżwiński\Projekty portfolio\Web Scraping\Data\APIdata', header=True)
        print("Data file created.")
    else:
        df.to_csv(r'C:\Marcin Łyżwiński\Projekty portfolio\Web Scraping\Data\APIdata', mode='a', header=False)
        print("Data file updated.")



if __name__ == "__main__":
    update_data()


