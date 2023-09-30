import os
import re
import json
import requests
from bs4 import BeautifulSoup


def fetch_categories():
    url = 'https://www.moderndatastack.xyz/categories'
    categories = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('a', id=re.compile('^categoryCard'))
            for card in cards:
                h5_tag = card.find('h5')

                id = card['href'].split('/')[-1] if card else 'No ID available'
                name = h5_tag.text if h5_tag else 'No name available'
                categories.append(dict(id=id, name=name))
            return categories
        else:
            return f"Failed to fetch the webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"


def fetch_companies_by_category(category_id):
    url = 'https://www.moderndatastack.xyz/companies/' + category_id
    companies = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.select('div.card-body')
            for card in cards:
                a_tag = card.find('a')
                h5_tag = card.find('h5')

                id = a_tag['href'].split('/')[-1] if a_tag else 'No ID available'
                name = h5_tag.text if h5_tag else 'No name available'
                companies.append(dict(id=id, name=name, category_id=category_id))
            return companies
        else:
            return f"Failed to fetch the webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"


def fetch_stacks():
    url = 'https://www.moderndatastack.xyz/stacks'
    stacks = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('a', id=re.compile('^stackCard'))
            for card in cards:
                h4_tag = card.find('h4')
                vendors = card.find_all('a')

                id = card['href'].split('/')[-1] if card else 'No ID available'
                name = h4_tag.text if h4_tag else 'No name available'
                sub_stacks = []
                for vendor in vendors:
                    if not vendor['href'].startswith('/company'):
                        continue
                    vendor_id = vendor['href'].split('/')[-1] if vendor else 'No ID available'
                    sub_stacks.append(dict(id=id, name=name, vendor_id=vendor_id))
                stacks.extend(sub_stacks)
            return stacks
        else:
            return f"Failed to fetch the webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"


# # parse categories
categories = fetch_categories()

# # parse all companies in each category
vendors = []
for category in categories:
    vendors.extend(fetch_companies_by_category(category['id']))

# parse data stacks
stacks = fetch_stacks()

# Create the JSON file path
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
data_dir = os.path.join(parent_dir, 'raw_data')
categories_file_path = os.path.join(data_dir, 'categories.json')
vendors_file_path = os.path.join(data_dir, 'vendors.json')
stacks_file_path = os.path.join(data_dir, 'stacks.json')

# Write JSON files
with open(categories_file_path, 'w') as json_file:
    json.dump(categories, json_file, indent=4)

with open(vendors_file_path, 'w') as json_file:
    json.dump(vendors, json_file, indent=4)

with open(stacks_file_path, 'w') as json_file:
    json.dump(stacks, json_file, indent=4)
