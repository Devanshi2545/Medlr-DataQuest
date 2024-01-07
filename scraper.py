# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_pharmeasy_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Write the scraping code for PharmEasy
    name = soup.find('h1', {'class': '_2_2BON'}).text.strip()
    mrp = soup.find('div', {'class': '_30jeq3'}).text.strip()
    discounted_price = soup.find('div', {'class': '_3N5LkZ'}).text.strip()
    manufacturer = soup.find('div', {'class': '_1qA8ok'}).text.strip()
    salts = soup.find('div', {'class': '_1Xf-N8'}).text.strip()

    return name, mrp, discounted_price, manufacturer, salts, url

def scrape_netmeds_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Write the scraping code for NetMeds
    name = soup.find('h1', {'class': 'fn product-title'}).text.strip()
    mrp = soup.find('span', {'class': 'price'}).text.strip()
    discounted_price = soup.find('span', {'class': 'final-price'}).text.strip()
    manufacturer = soup.find('div', {'class': 'drug_manufacturer'}).text.strip()
    salts = soup.find('div', {'class': 'salt-composition'}).text.strip()

    return name, mrp, discounted_price, manufacturer, salts, url
