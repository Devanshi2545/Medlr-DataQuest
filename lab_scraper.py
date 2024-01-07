# lab_scraper.py
import requests
from bs4 import BeautifulSoup
import csv

def lab_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # Make a request to the specified URL
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting lab data
        lab_name = soup.find('h1', {'class': 'title'}).text.strip()
        mrp = soup.find('span', {'class': 'price-regular'}).text.strip()
        discounted_price = soup.find('span', {'class': 'price'}).text.strip()

        # Extracting tests included
        tests_included = [test.text.strip() for test in soup.find_all('div', {'class': 'package-test-item'})]

        # Extracting lab address
        address = soup.find('div', {'class': 'lab-address'}).text.strip()

        return lab_name, mrp, discounted_price, tests_included, address

    else:
        return f"Failed to fetch data. Status Code: {response.status_code}"

if __name__ == "__main__":
    # Example URLs
    lab_urls = [
        "https://www.labuncle.com/packages/good-health-package-1433",
        "https://www.labuncle.com/packages/health-champion-radiology-package-1677",
        # Add more LabUncle URLs as needed
    ]

    lab_data = [lab_scraper(url) for url in lab_urls]

    # Writing data to CSV file
    csv_filename = "lab_data.csv"
    header = ["Lab Name", "MRP", "Discounted Price", "Tests Included", "Address"]

    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(lab_data)

    print(f"Data written to {csv_filename}")
