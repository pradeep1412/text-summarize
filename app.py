from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/summarizer')
def search():
    lang = request.args.get('max_len', '130')  
    country = request.args.get('min_len', '30') 
    context = request.args.get('context') 

    if not query:
        return jsonify({"error": "Missing 'context' parameter."}), 400

    return summarizer(context, max_length=130, min_length=30, do_sample=False)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)

