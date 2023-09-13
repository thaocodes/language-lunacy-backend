from flask import Blueprint, jsonify
from scraper import scrape_words

words_bp = Blueprint("words", __name__, url_prefix="/words")

@words_bp.route("/<language>", methods=["GET"])
def get_words(language):
    try:
        words = scrape_words(language)
        return jsonify(words), 200
    except Exception as e: 
        # extract error message string from exception object
        return jsonify(error=str(e)), 404




