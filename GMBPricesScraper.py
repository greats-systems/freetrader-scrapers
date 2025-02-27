import pandas as pd
import os
import numpy as np
from dotenv import load_dotenv
from supabase import create_client, Client

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

load_dotenv()

URL = os.getenv('URL')
ANON_KEY = os.getenv('ANON_KEY')
SERVICE_KEY = os.getenv('SERVICE_KEY')

root = 'https://www.gmbdura.co.zw/index.php/grain-prices/producer-prices'

df = pd.read_html(root)[0]
cols = list(df.iloc[0].values)
cols[1]=''.join(cols[1].split())

df.rename(columns={0: cols[0], 1: cols[1]}, inplace=True)
df=df.iloc[1:]
df.reset_index(drop=True, inplace=True)
df.replace(np.nan, '', inplace=True)

supabase: Client = create_client(URL, ANON_KEY)

for row in df.iterrows():
    supabase.table("Commodities").insert({"CommodityName":row[1][0], "CommodityPrice":row[1][1]}).execute()





