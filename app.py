from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Veri ve model yükleme
dataDF = pd.read_csv("cleaned_data_son.csv")

def convert_string_to_list(embedding_str):
    return np.array(eval(embedding_str), dtype=np.float32)

dataDF['embedding'] = dataDF['embedding'].apply(convert_string_to_list)
embeddings_list = np.array(dataDF['embedding'].tolist())
embeddings_tensor = torch.tensor(embeddings_list, dtype=torch.float32)

tokenizer = AutoTokenizer.from_pretrained('dbmdz/bert-base-turkish-uncased')
model = AutoModel.from_pretrained('dbmdz/bert-base-turkish-uncased')

# Stop words list (örnek olarak bazı ifadeler eklendi)
STOP_WORDS = [
    "atasözü öner", "deyim öner", "söz öner", 
    "öner", "yardım", "lütfen", "başka bir şey"
]

def preprocess_input(text):
    # Stop words listesiyle metni temizleyin
    for stop_word in STOP_WORDS:
        text = text.replace(stop_word, "")
    return text.strip()

def get_lemmatize_words(text):
    # Burada lemmatizasyon işlemini yapın
    return text

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def get_input_embedding(text):
    text = preprocess_input(text)
    text = get_lemmatize_words(text)
    embedding = get_embedding(text)
    if embedding.ndim == 3:
        embedding = embedding.mean(dim=1)
    return embedding

def find_top_n_similar_quotes(input_text, dataDF, n=5):
    input_embedding = get_input_embedding(input_text).numpy()
    embeddings = np.array(dataDF['embedding'].tolist())
    if embeddings.ndim == 3:
        embeddings = embeddings.mean(axis=1)
    similarities = cosine_similarity(input_embedding, embeddings)
    most_similar_indices = np.argsort(similarities[0])[::-1][:n]
    top_quotes = dataDF.iloc[most_similar_indices][['sozum', 'anlami']]
    return top_quotes.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_input = data.get('text', '')
    top_quotes = find_top_n_similar_quotes(user_input, dataDF)
    return jsonify(top_quotes)

if __name__ == '__main__':
    app.run(debug=True)

