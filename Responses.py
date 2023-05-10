from datetime import datetime
from bs4 import BeautifulSoup
import requests

def sample_resposes(input_text):
    user_message = str(input_text).lower()

    if user_message in ("merhaba" ):
        return "hey!!!"
    if user_message in ("sen kimsin"):
        return "asistan"
    if user_message in ("tarih"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, saat %H:%M:%S" )

        return str(date_time)
def ar_resposes(input_text):
    user_message=str(input_text).lower()
    if user_message in ("eczane"):
        return 


    return "seni anlamadım"