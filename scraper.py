from flask import Flask
from bs4 import BeautifulSoup
import requests

def scrape_words(language):
    '''
    Fetches a list of common words in the specified language along with their English translations.
    
    Args: 
    language (string): The target language for fetching the words.

    Returns:
    words (array): A list of dictionary objects containing words in the specified language and English.
    '''
    language = language.lower()
    url = f'https://1000mostcommonwords.com/1000-most-common-{language}-words/'
    response = requests.get(url)

    if response.status_code == 404:
        raise Exception(f"No list of words for this language '{language.capitalize()}'")
        
    # parse response (webpage)
    soup = BeautifulSoup(response.text, 'html.parser')

    words = []

    # find all table rows, excluding header row
    rows = soup.find_all('tr')[1:]
    for row in rows:
        columns = row.find_all('td')[1:3]    # get only the columns with words
        if len(columns) == 2:                # ensure we have both words
            words.append({
                language: columns[0].text,    # first column is {language} word
                "english": columns[1].text,   # second column is english translation 
                "difficulty": "unset"
            })

    return words
            

    