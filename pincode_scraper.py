# pincode_scraper.py
import requests
from bs4 import BeautifulSoup
import time

def scrape_medicine_availability(pincode, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # Make a request to the specified URL
    response = requests.get(url, headers=headers)
    
    # Sleep to avoid being blocked by the website
    time.sleep(5)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting delivery date
        delivery_date = soup.find('div', {'class': 'availability-status'}).text.strip()

        return delivery_date, pincode, url

    else:
        return f"Failed to fetch data. Status Code: {response.status_code}", pincode, url

if __name__ == "__main__":
    # User input
    user_pincode = input("Enter Pincode: ")
    user_url = input("Enter Medicine URL: ")

    result = scrape_medicine_availability(user_pincode, user_url)

    print("Result:", result)
