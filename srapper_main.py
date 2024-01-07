#srapper_main.py
# main.py
from scraper import scrape_pharmeasy_data, scrape_netmeds_data

pharmeasy_urls = [
    "https://pharmeasy.in/online-medicine-order/ferimuna-xt-susp-200ml-166294",
    "https://pharmeasy.in/online-medicine-order/lactofol-cap-10-s-191885",
    # Add more PharmEasy URLs as needed
]

netmeds_urls = [
    "https://www.netmeds.com/prescriptions/mednocal-tablet-10s",
    # Add more NetMeds URLs as needed
]

for url in pharmeasy_urls:
    data = scrape_pharmeasy_data(url)
    print(data)

for url in netmeds_urls:
    data = scrape_netmeds_data(url)
    print(data)
