#!/bin/python
import os
import datetime

def url() -> str:
    return "https://www.merriam-webster.com/word-of-the-day/calendar"

def today() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_wotd_element(url, date):
    os.system(f"curl -s {url} | grep '{date}'")

if __name__ == "__main__":
    get_wotd_element(url(), today())
