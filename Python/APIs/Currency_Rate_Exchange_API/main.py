from flask import Flask, jsonify, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])

    return rate

@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
