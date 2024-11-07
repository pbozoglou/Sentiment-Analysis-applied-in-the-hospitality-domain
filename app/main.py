import pandas as pd
from app.utils.config import PLACES_API_KEY
import requests

def main():
    url=''
    r = requests.get(url)
    print(r.content)

if __name__ == "__main__":
    main()