<div align="center">
<pre>
 ▄▀▀ ▀█▀ ▄▀▄ ▄▀▀ █▄▀ █   █ █ ▄▀▀ ██▀   █▀▄ ▄▀▄ █ █ ▀▄▀
 ▄██  █  ▀▄▀ ▀▄▄ █ █ ▀▄▀▄▀ █ ▄██ █▄▄   █▄▀ █▀█ █ █▄ █                  
-------------------------------------------------------
python program that sends daily stock updates to your email
</pre>

[![PyPI](https://img.shields.io/pypi)](https://pypi.org/project/stockwise-daily/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

Stockwise Daily sends you personalized daily emails with stock performance updates, relevant news, and more--keeping you informed and entertained in one quick read.

## Features

- Daily stock performance summaries for selected companies
- Relevant news articles based on stock symbols
- Customizable email content


## Installation

Clone this repo and install dependencies listed in requirements.txt

```sh
git clone https://github.com/escharry/stockwise-daily.git
```

```sh
cd stockwise-daily
pip3 install -r requirements.txt
```

## Set up API keys

```sh
STOCK_API_KEY='your_stock_api_key'
NEWS_API_KEY='your_news_api_key'
EMAIL_CREDENTIALS={"sender": "your_email@example.com", "password": "your_password"}
```

## How it works
- Stocks: Fetches stock data for predefined symbols
- News: Pulls related articles based on such symbols
- Email: Sends the update via email using SMTP

## Meta

Esteban Charry – echarry@berkeley.edu

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/escharry/](https://github.com/escharry/)

## Contributing

1. Fork it (<https://github.com/escharry/stockwise-daily/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
