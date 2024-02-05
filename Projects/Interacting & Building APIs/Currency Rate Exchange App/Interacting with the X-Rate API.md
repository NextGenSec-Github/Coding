# Building a Currency Converter with Flask - Step by Step

![](https://github.com/yusufmunircloud/AWS-Projects/blob/main/img/general/Screenshot%202024-02-05%20185335.png?raw=true)

## Step 1: Importing Libraries and Initializing Flask
```python
from flask import Flask, jsonify, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
```

- **Flask:** It's a web framework for Python, used to build web applications.
- **BeautifulSoup:** A library for web scraping. It helps parse HTML and extract information.
- **requests:** Used for making HTTP requests.

## Step 2: Creating a Function to Fetch Exchange Rates

```python
def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])

    return rate
```

- The get_currency function takes two currency codes (in_currency and out_currency) as parameters.
- It constructs a URL to fetch the exchange rate from x-rates.com.
- It makes a request to the website, gets the HTML content, and parses it using BeautifulSoup.
- It extracts the exchange rate from the HTML using the specified class (ccOutputRslt).
- The rate is converted to a float after removing the unnecessary characters.
