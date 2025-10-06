import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://catalog.data.gov/dataset?q=real+estate&sort=metadata_created+desc"

response = requests.get(url)
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to fetch page:", response.status_code)
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

dataset_titles = []
dataset_links = []
dataset_descriptions = []

for dataset in soup.find_all('h3', class_='dataset-heading'):
    title = dataset.text.strip()
    link = "https://catalog.data.gov" + dataset.find('a')['href']
    dataset_titles.append(title)
    dataset_links.append(link)

for desc in soup.find_all('div', class_='notes'):
    description = desc.text.strip()
    dataset_descriptions.append(description)

min_length = min(len(dataset_titles), len(dataset_descriptions))
data = {
    'Title': dataset_titles[:min_length],
    'Description': dataset_descriptions[:min_length],
    'Link': dataset_links[:min_length]
}

df = pd.DataFrame(data)

df.to_csv('datasets.csv', index=False)

print("Data saved to 'datasets.csv")