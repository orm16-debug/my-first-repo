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
conda create -n my-frist-env python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
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


## Testing

Run tets:
```sh
pytest
```