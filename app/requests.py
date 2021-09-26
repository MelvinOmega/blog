from config import Config
from . models import Quotes
import requests,json

quotes_url = Config.QUOTES_URL

def getQuotes():
    random_quote = requests.get(quotes_url)
    new_quote = random_quote.json()
    author = new_quote.get("author")
    quote = new_quote.get("quote")
    permalink = new_quote.get("permalink")
    quote_object = Quotes(author,quote,permalink)
    print(quote_object)
    return quote_object


def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        return quote    