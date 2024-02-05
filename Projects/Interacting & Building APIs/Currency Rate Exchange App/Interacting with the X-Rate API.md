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

## Step 3: Setting Up the Home Route

```python
@app.route('/')
def home():
    return render_template('index.html')
```

- The '/' route renders the index.html template. This is the home page of the application.

## Step 4: Handling Currency Conversion

```python
@app.route('/convert', methods=['POST'])
def convert():
    input_currency = request.form['input_currency']
    output_currency = request.form['output_currency']
    rate = get_currency(input_currency, output_currency)

    result_dictionary = {
        'input_currency': input_currency,
        'output_currency': output_currency,
        'rate': rate
    }

    return render_template('index.html', result=result_dictionary)
```

- The '/convert' route is activated when the form on the home page is submitted.
- It retrieves the input and output currencies from the form.
- Calls the get_currency function to get the exchange rate.
- Creates a dictionary with the input currency, output currency, and the rate.
- Renders the index.html template with the result.

## Step 5: Running the Application

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

- Checks if the script is the main program.
- If so, it starts the Flask development server with the specified host ('0.0.0.0') and in debug mode.

## Conclusion

This code covered the initialization of a Flask application, fetching real-time exchange rates using web scraping, setting up routes, handling form submissions, and rendering templates. Users can access the currency converter web application by running the script and visiting http://127.0.0.1:5000/ in their web browser. NOTE: I have put the index.html and style.css files within this directory for use.

