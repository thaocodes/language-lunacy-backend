from flask import Flask
from bs4 import BeautifulSoup
import requests

def scrape_words(language, start=0, end=100):
    '''
    Fetches a subset of words in a specified language along with their English translations
    
    Args: 
    language (string): Target language for fetching words
    start (integer): Starting index of the range (inclusive)
    end (integer): Ending index of the range (exclusive)

    Returns:
    words (array): List of word dictionaries with word details
    '''
    language = language.lower()

    if start < 1 or end > 1000 or start >= end: 
        raise ValueError("Invalid start or end value. Valid range is 0-1000 and start should be less than end.")
    
    url = f'https://1000mostcommonwords.com/1000-most-common-{language}-words/'
    response = requests.get(url)

    if response.status_code == 404:
        raise Exception(f"No list of words for this language '{language.capitalize()}'")
        
    # parse response (webpage)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all table rows, excluding header row
    rows = soup.find_all('tr')[1:]

    words = []
    for row in rows[start - 1:end]:
        columns = row.find_all('td')
        if len(columns) == 3:
            words.append({
                "number": int(columns[0].text),
                language: columns[1].text,
                "english": columns[2].text,
                "difficulty": "unset"
            })

    return words
            

    