# my-first-repo

Version control exercise

editing in VS

Adding content using VS code editor

# My First Repo!

This is the README.md file. It uses the markdown language.

Here is a list:

  + Item 1
  + Item 2
  + Item 3

For more information about Markdown syntax, see the [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).

## Setup

Clone the repo to download it from GitHub. Perhaps onto the Desktop.

Navigate to the repo using the command line.

```sh
cd ~/Desktop/my-first-repo
```

Create a virtual environment:
```sh
conda create -n my-first-env python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

The stocks functionality requires an AlphaVantage API Key. Obtain a premium AlphaVantage API Key (using [form](https://www.alphavantage.co/support/#api-key))

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file

ALPHAVANTAGE_API_KEY = "__________"

# also tell the file

FLASK_APP=web_app

```

## Usage

Example script:

```sh
python app/my_script.py
```

Game of Rock, Paper, Scissors:

```sh
python app/rps.py

# alternative "modular style" command:
python -m app.rps
```

Stocks dashboard:

```sh
python -m app.stocks
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# if we have the FLASK_APP=web_app env var in the ".env" file:
flask run 

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tets:
```sh
pytest
```

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run