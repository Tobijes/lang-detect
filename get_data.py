import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

wiki_languages = pd.read_csv("wiki_languages.csv")


N = 5000
results = []
for i in tqdm(range(N)):
    row = wiki_languages.sample()
    language_name = row["Language"].values[0]
    language_code = row["Wiki"].values[0]

    url = f"https://{language_code}.wikipedia.org/wiki/Special:Random"
 
    # Fetch URL Content
    r = requests.get(url)

    # Get body content
    soup = BeautifulSoup(r.text,'html.parser').select('body')[0]
    for tag in soup.find_all("p"):

        text = tag.text

        if len(text) < 10:
            continue        
       
        result = {
            "url": r.url, 
            "text" : text,
            "language_code": language_code,
            "language_name": language_name
        }
        results.append(result)


print("Number of results:", len(results))

df = pd.DataFrame(results)

df.to_parquet(f'data/data_{N}.parquet', engine='pyarrow')