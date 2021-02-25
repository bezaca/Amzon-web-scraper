# Basic Amazon Web Scrapper

This code is made for a basic web scraper using Beautifulsoup and requests , that it's capable to notify via email when a price change.

## Getting Started

To run this project you will need to set your environment variables.

1. Create a new file named `.env` inside the `module` folder.
2. Copy all of the variables inside `module/.template.env` and assign your own values to them.

Also , you will need to install all the packages needed for this project , running the next command:

```
pip install -r requirements.txt
```

### `NOTE`: 

I recommend to create a virtual environment for this project , you can do it by running:
```
python -m venv env (or change 'env' for the name you want)
```

Then after completing all the configuration steps , you are ready to run this code by tipping:
```
python main.py
```


### `Recommendations:`

As a safeguard against putting your email password , you can generate a one-time password using the Google app password service (if you're usign gmail) , following the next steps:

1. Activate your `two-step verification` on your google account
2. Search for `google app password`
3. Generate a password for `Mail` and `Windows Computer`
4. Use that generate password for `SENDER_EMAIL_PASSWORD` in your `.env` file





