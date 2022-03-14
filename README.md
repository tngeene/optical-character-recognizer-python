# Captcha solving using Pytesseract and Pillow

> An image text recognition program

## Setup and Requirements

Ensure you have [poetry](https://python-poetry.org/docs/) and python 3.9 installed.

To do this run `pip3 install poetry`

Navigate to the project repo and run

    poetry install
After all dependencies have been installed, run the script by

    python main.py --i "https://imgur.com/USc3mUY.jpg"

where the argument after --i flag is the path to a captcha file.
