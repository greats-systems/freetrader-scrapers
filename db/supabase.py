from supabase import Client, create_client
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
ANON_KEY = os.getenv('ANON_KEY')
SERVICE_KEY = os.getenv('SERVICE_KEY')

def create_supabase_client():
    supabase: Client = create_client(URL, SERVICE_KEY)
    return supabase
