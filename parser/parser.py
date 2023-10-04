import json
import requests
import logging
import tqdm  # Import the tqdm module for progress indication

from bs4 import BeautifulSoup
from pathlib import Path

logging.basicConfig(level=logging.ERROR)

def fetch_webpage(url):
    """Fetches the webpage content from the specified URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch the webpage: {e}")
        return None

def parse_data(html_text, key):
    """Parses the HTML content to extract data based on a specified key."""
    soup = BeautifulSoup(html_text, 'html.parser')
    data_tag = soup.find('script', {'id': '__NEXT_DATA__'})
    if data_tag is not None:
        data = json.loads(data_tag.text)
        result = data.get('props', {}).get('pageProps', {}).get(key)
        if result is not None:
            return result
    return []

def fetch_categories():
    """Fetches the categories of data from the website."""
    url = 'https://www.moderndatastack.xyz/categories'
    html_text = fetch_webpage(url)
    if html_text is not None:
        return parse_data(html_text, 'categories')
    return []

def fetch_companies_by_category(category_slug):
    """Fetches companies data by category from the website."""
    url = f'https://www.moderndatastack.xyz/companies/{category_slug}'
    html_text = fetch_webpage(url)
    if html_text is not None:
        companies = parse_data(html_text, 'companies')
        for company in companies:
            company['categorySlug'] = category_slug
        return companies
    return []

def fetch_stacks():
    """Fetches stacks of data from the website."""
    url = 'https://www.moderndatastack.xyz/stacks'
    html_text = fetch_webpage(url)
    if html_text is not None:
        return parse_data(html_text, 'stacks')
    return []

def fetch_all_data():
    """Fetches all the necessary data from the website."""
    # Parse categories
    categories = fetch_categories()

    # Parse all companies in each category
    vendors = []
    for category in tqdm.tqdm(categories, desc="Fetching companies by category"):  # Add progress indication here
        vendors.extend(fetch_companies_by_category(category['slug']))

    # Parse data stacks
    stacks = fetch_stacks()

    return categories, vendors, stacks

def save_to_json(data, filename):
    """Saves the specified data to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f'Data saved to {filename}')
    except Exception as e:
        print(f'An error occurred while saving the data: {e}')

if __name__ == '__main__':
    # Fetch all data from the website
    categories, vendors, stacks = fetch_all_data()

    # Create the JSON file path
    current_script_dir = Path(__file__).resolve().parent
    data_dir = current_script_dir.parent / 'raw_data'
    data_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

    # Define file paths
    categories_file_path = data_dir / 'categories.json'
    vendors_file_path = data_dir / 'vendors.json'
    stacks_file_path = data_dir / 'stacks.json'

    # Write JSON files
    save_to_json(categories, categories_file_path)
    save_to_json(vendors, vendors_file_path)
    save_to_json(stacks, stacks_file_path)
