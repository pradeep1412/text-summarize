import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def text_summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum()]
    
    stopwords_en = set(stopwords.words('english'))
    words = [word for word in words if word not in stopwords_en]
    
    freq_dist = FreqDist(words)
    ranking = {}
    for i, sentence in enumerate(sentences):
        for word, freq in freq_dist.items():
            if word in sentence.lower():
                if i in ranking:
                    ranking[i] += freq
                else:
                    ranking[i] = freq
    
    sorted_sentences = sorted(ranking, key=ranking.get, reverse=True)
    summarized_sentences = [sentences[i] for i in sorted_sentences[:num_sentences]]
    summarized_text = ' '.join(summarized_sentences)
    return summarized_text

# Example text
input_text = """
Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to read, decipher, understand, and make sense of human language in a way that is valuable. NLP has applications in many areas, including language translation, sentiment analysis, chatbots, and text summarization.
"""

num_sentences = 2
summary = text_summarize(input_text, num_sentences)
print(summary)
