# language-lunacy-backend
Backend Flask App for Language Lunacy: where web scraping meets fun and effective language learning :D

## Overview

This repository hosts the backend component of a language learning flashcard application. The Flask-based backend provides an API that fetches a range of common words in specified languages along with their English translations from a source website to aid in language learning through flashcards.

## Features
- **GET Words Endpoint**: Fetch a specific range of words in a specified language to assist users in learning new languages through flashcards.
- **Error Handling**: Effective error handling to manage potential issues like invalid language input or range specifications.



  
## API Endpoints  
- **GET** `/words/<language>/<start>/<end>`: Fetches a range of words (from `start` to `end`) in the specified `language`. Returns a list of words with details or an error message in JSON format.

## Setup and Installation  
1. Clone the repository.
2. Install the necessary Python packages: **`pip install -r requirements.txt`**.
3. Run the Flask application: **`flask run`**

## Usage  
To use the API, make a GET request to the endpoint with the appropriate parameters, for example:

http://127.0.0.1:5000/words/dutch/100/200

#### Happy Language Learning! 
