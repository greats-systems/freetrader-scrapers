import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

load_dotenv()

URL = os.getenv('URL')
ANON_KEY = os.getenv('ANON_KEY')
SERVICE_KEY = os.getenv('SERVICE_KEY')

root = 'https://www.gmbdura.co.zw/index.php/grain-prices/producer-prices'

class GMBScraper:
    def scrape():
        df = pd.read_html(root)[0]
        cols = list(df.iloc[0].values)
        cols[1]=''.join(cols[1].split())

        df.rename(columns={0: cols[0], 1: cols[1]}, inplace=True)
        df=df.iloc[1:]
        df.reset_index(drop=True, inplace=True)
        df.replace(np.nan, None, inplace=True)
        df['ProducerPrice']=df['ProducerPrice'].map(
            lambda x: str(x)[1:]
            if str(x)[0]=='$'
            else x
        )

        supabase: Client = create_client(URL, SERVICE_KEY)

        for row in df.iterrows():
            supabase.table("Commodities").insert({"CommodityName":row[1][0], "CommodityProducePrice":row[1][1]}).execute()
        return 'Success!'







