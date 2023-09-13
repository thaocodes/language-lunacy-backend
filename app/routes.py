from flask import Blueprint, jsonify
from scraper import scrape_words

words_bp = Blueprint("words", __name__, url_prefix="/words")

@words_bp.route("/<language>/<int:start>/<int:end>", methods=["GET"])
def get_words(language, start, end):
    """
    Endpoint to fetch a range of words in a specified language using the scrape_words function
    
    Args:
    language (str)
    start (int), end (int): Ehe range of words to retrieve
    
    Returns:
    JSON: list of words and details, or an error message
    """
    try:
        words = scrape_words(language, start, end)
        return jsonify(words), 200
    except ValueError as e:
        return jsonify(error=str(e))
    except Exception as e: 
        # extract error message string from exception object
        return jsonify(error=str(e)), 404
    




