from bs4 import BeautifulSoup
import pandas as pd

def extract_table_after_headline(file_path, headline_text):
    # Read the HTML file
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the specific headline
    headline = soup.find_all(text=headline_text)

    if not headline:
        print("Headline not found.")
        return None

    # Find the next table after the headline
    for h in headline:
        next_table = h.find_next('table')
        if next_table:
            # Convert the table to a DataFrame
            df = pd.read_html(str(next_table))[0]
            return df

    print("No table found after the headline.")
    return None

# Example usage
file_path = 'wiki_langs.txt'
headline_text = 'All Wikipedias ordered by number of articles'
df = extract_table_after_headline(file_path, headline_text)

df.to_csv("wiki_languages.csv")