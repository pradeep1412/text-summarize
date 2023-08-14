from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/summarizer')
# def search():
#     num_sentences = request.args.get('num_sentences', '2')
#     context = request.args.get('context') 

#     if not context:
#         return jsonify({"error": "Missing 'context' parameter."}), 400

#     return text_summarize(context, int(num_sentences))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)

