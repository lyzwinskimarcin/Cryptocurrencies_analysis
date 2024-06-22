import pandas as pd
import os

def archive_data():
    archive_date = pd.to_datetime('now') - pd.DateOffset(days=30)
    
    df = pd.read_csv(r'C:\Marcin Łyżwiński\Projekty portfolio\Web Scraping\Data\APIdata')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    new_df = df[df['timestamp'] > archive_date]
    new_df.to_csv(r'C:\Marcin Łyżwiński\Projekty portfolio\Web Scraping\Data\APIdata', mode='w', header=True)

if __name__ == "__main__":
    archive_data()