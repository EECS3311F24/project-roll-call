from ..services.gemini_service.word_gen import WordGen
from ..services.gemini_service.quote_gen import QuoteGen
from flask import jsonify 

from . import gem

@gem.route("/generate_word", methods=['GET'])
def get_word():
    word_gen = WordGen()
    word = word_gen.get_word()
    return jsonify(word)

@gem.route("/generate_quote", methods=['GET'])
def get_quote():
    quote_gen = QuoteGen()
    quote = quote_gen.get_quote()
    return jsonify(quote)
